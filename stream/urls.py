from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', home, name='streams'),
    url(r'^(\d+)', get_stream, name='stream'),
    url(r'^catagory/(\d+)', get_catagory, name='streamcatagory'),
    
]
