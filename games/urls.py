from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^home/$', Home, name='games'),
    url(r'^game/(\d+)', get_game, name='game'),
    url(r'^publisher/(\d+)', get_publisher, name='publisher'),
    url(r'^gamecreate/', add_game, name='addgame'),
    url(r'^publishercreate/', add_publisher, name='addpublisher'),
    
    
    
]
