from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^game/(\d+)/', review_game, name='reviewgame'),
    
    
]
