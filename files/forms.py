from django import forms
from .models import TableFile
from django.core.validators import FileExtensionValidator


class TableFileForm(forms.ModelForm):

   class Meta:
      model = TableFile
      fields = ['id','name','file']

class PagesForm(forms.Form):
   page = forms.IntegerField(min_value=1)
   paginate_by = forms.IntegerField(min_value=1)