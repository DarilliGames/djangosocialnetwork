from django.db import models
from games.models import Game

class Stream(models.Model):
    streamer = models.ForeignKey("auth.user")
    streamkey = models.CharField(max_length=100, blank=False, default="darilli")
    game = models.ForeignKey(Game)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.streamer.username
