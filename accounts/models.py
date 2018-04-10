from django.db import models
from django.contrib.auth.models import User
from games.models import *

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="uprofile")
    playing_game = models.ForeignKey(Game, null=True, blank=True, on_delete=models.CASCADE, related_name="streamers")
    header = models.CharField(max_length=200, blank=True)
    bio = models.TextField()
    is_youtube = models.BooleanField(default=False)
    youtubelink = models.CharField(max_length=200, blank=True)
    is_streamer = models.BooleanField(default=False)
    streamkey = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)
    join_date = models.DateField(auto_now_add=True)
    last_online = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
        
class CharacterProfile(models.Model):
    
    userprofile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cprofile")
    character = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="cgame")
    serious =models.BooleanField(default=True)
    fun =models.BooleanField(default=True)
    rank = models.IntegerField(blank=True, default=0)
    
    def __str__(self):
        return self.character