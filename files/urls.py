from django.contrib.auth import login
from django.urls import path
from .views import (
    upload_file, 
    TableFileCreateView, 
    TableFileDeleteView, 
    TableFileDetailView,
    )
    


urlpatterns = [
    path('', upload_file, name = "files" ),
    path('tablefile_form/', TableFileCreateView.as_view(), name = 'tablefile_form'),    
    path('<int:pk>/tablefile_detais/<str:slug>/<int:current_page>/<int:sort_order>/<int:next_page>/<int:prev_page>/<int:paginate_by>/', TableFileDetailView.as_view(), name = 'tablefile_details'),   
    path('<int:pk>/tablefile_confirm_delete/',TableFileDeleteView.as_view(), name = 'tablefile_delete'),   
]