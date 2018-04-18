from django.db import models
from django.contrib.auth.models import User
from games.models import *



league_ranks = { 0:"Unranked", 1:"Bronze 3 or less", 2:"Bronze 1", 3:"Silver 3", 4:"Silver 1", 5:"Gold 3", 6:"Gold 1", 7:"Platinum 3", 8:"Platinum 1", 9:"Diamond 3", 10:"Diamond 1", 11:"Masters", 12:"Challenger"}

wow_ranks = { 0: "Unranked", 1:"<1200", 2:"1200-1600", 3:"1600-1800", 4:"1800-2000", 5:"2000-2200", 6:"2200-2400", 7:"2400-2600", 8:"2600-2800", 9:"2800+"}

# { 0: "Unranked", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:"", 10:"", 11:"", 12:""}



def rankify(game, rank):
    if game.id == 1:
        return league_ranks[rank]
    if game.id == 3:
        return wow_ranks[rank]
    else:
        return str(rank)



class CharacterProfile(models.Model):
    
    userprofile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cprofile")
    character = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="cgame")
    serious =models.BooleanField(default=True)
    fun =models.BooleanField(default=True)
    rank = models.IntegerField(blank=True, default=0)
    
    def __str__(self):
        return self.character
        
    def get_rank(self):
        return rankify(self.game, self.rank)

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
    main_character = models.OneToOneField(CharacterProfile, null=True, blank=True, on_delete=models.CASCADE, related_name="maincharacter")
    img_profile = models.ImageField(upload_to='media', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
        
class Attributes(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="attributes")
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name+"("+self.game.name+")"
    
class AttributeValue(models.Model):
    value = models.CharField(max_length=100)
    attribute = models.ForeignKey(Attributes, on_delete=models.CASCADE, related_name="attribute")
    def __str__(self):
        return self.value
    
class AttributeChoices(models.Model):
    name = models.ForeignKey(AttributeValue, on_delete=models.CASCADE, related_name="attributechoice")
    character = models.ForeignKey(CharacterProfile, on_delete=models.CASCADE, related_name="abouts")
    
    def __str__(self):
        return self.name.value
    

    