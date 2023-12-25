from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, FormMixin
from django.views.generic.detail import DetailView
from math import ceil
from pandas import read_csv

from .forms import TableFileForm, PagesForm
from .models import TableFile


class TableFileCreateView(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login/"
    redirect_field_name = "files"
    
    model = TableFile
    fields = ['id', 'name', 'file']

class TableFileDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/accounts/login/"
    redirect_field_name = "files"
    
    model = TableFile
    success_url = reverse_lazy('files')

class TableFileDetailView(LoginRequiredMixin, FormMixin, DetailView):
    login_url = "/accounts/login/"
    redirect_field_name = "tablefile_details"

    model = TableFile   
    form_class = PagesForm
    

    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)       
        
        # параметр slug носит значение либо имени файла, либо имени столбца, по которому производится сортировка таблицы
        slug = self.kwargs.get('slug')
        # порядок сортировки: прямой или обратный  
        ascending = bool(int(self.kwargs.get('sort_order')))        
        
        # чтение таблицы как датафрейма pandas
        df = read_csv(context['object'].file)       
        current_page = self.kwargs.get('current_page')
        paginate_by = self.kwargs.get('paginate_by')
        num_pages = ceil(len(df)/paginate_by)
        context['paginate_by'] = paginate_by
            
        # функция пагинации таблицы датафрейма
        def paginate_dataframe(dataframe, page_size, page_num):
            page_size = page_size
            if not page_num:
                page_num = 1
            offset = page_size * (int(page_num) - 1)          
            return dataframe[offset:offset + page_size]

        if slug != slugify(context['object'].name):                       
            df = df.sort_values(by=slug, ascending=ascending)                

        context['page_obj'] = {'previous_page_number': 0, 'next_page_number': 2, 'num_pages': num_pages, 'current_page': current_page}

        if self.kwargs.get('next_page') == 1:            
            current_page += 1
            context['page_obj']['current_page'] = context['page_obj']['current_page'] + 1
        
        if self.kwargs.get('prev_page') == 1:            
            current_page -= 1
            context['page_obj']['current_page'] = context['page_obj']['current_page'] - 1

        if self.kwargs.get('current_page') > num_pages:                     
            current_page = num_pages
            context['page_obj']['current_page'] = num_pages        
        
        context['df'] = paginate_dataframe(df, paginate_by, current_page)   
        
        if ascending == True:
            context['sort_order'] = '0'           
        elif ascending == False:
            context['sort_order'] = '1'
           
        return context
    
    # отрисовка текущих значений в полях формы выбора страницы и пагинации
    def get_initial(self, **kwargs):        
        initial = super().get_initial() 
        initial['page'] = self.kwargs['current_page'] + self.kwargs['next_page'] - self.kwargs['prev_page']                
        initial['paginate_by'] = self.kwargs['paginate_by']
        return initial

    def get_success_url(self):          
        return reverse("tablefile_details", kwargs=self.kwargs)    
   
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()        
        form = self.get_form()    
            
        if form.is_valid():                                  
            self.kwargs['current_page'] = form.cleaned_data.get("page")
            self.kwargs['paginate_by'] = form.cleaned_data.get("paginate_by")
            self.kwargs['next_page'] = self.kwargs['prev_page'] = 0            
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):        
        return super().form_valid(form)
    
    
# представление загрузки новых файлов и отображения списка уже загруженных
@login_required
def upload_file(request):
    if request.method == 'POST':        
        form = TableFileForm(request.POST, request.FILES)        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('files')) 
        else:
            files = TableFile.objects.order_by('name')            
            return render(request, 'files/uploads.html', {'form':form, 'files': files})
    else:
        form = TableFileForm
        files = TableFile.objects.order_by('name')
    return render(request, 'files/uploads.html', {'form':form, 'files': files})
