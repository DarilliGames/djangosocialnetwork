from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^home/$', Home, name='chat'),
    url(r'^post/$', Post, name='postchat'),
    url(r'^messages/$', Messages, name='messages'),
    url(r'^getchat/(\d+)/$', PGet, name='pget'),
    url(r'^chat/(\d+)/$', PChat, name='pchat'),
    url(r'^ppost/(\d+)/$', PPost, name='ppost'),
    url(r'^pmessage/(\d+)/$', PMessages, name='pmessages'),
    
]
