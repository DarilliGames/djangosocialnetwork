from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', search, name='search'),
    url(r'^games/$', search_games, name='sgames'),
    url(r'^users/$', search_users, name='susers'),
    url(r'^characters/(\d+)', search_characters, name='scharacters'),
    
]
