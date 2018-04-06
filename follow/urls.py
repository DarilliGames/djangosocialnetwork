from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^follow/(\d+)', follow_user, name='follow'),
    url(r'^unfollow/(\d+)', unfollow_user, name='unfollow'),
]