from django.db import models
from django.contrib.auth.models import User
from games.models import *

no_ranks = {0:"No Ranks Available"}

league_ranks = { 0:"Unranked", 1:"Bronze 3 or less", 2:"Bronze 2", 3:"Bronze 1", 4:"Silver 5", 5:"Silver 4", 6:"Silver 3", 7:"Silver 2", 8:"Silver 1", 9:"Gold 5", 10:"Gold 4", 11:"Gold 3", 12:"Gold 2", 13:"Gold 1", 14:"Platinum 5", 15:"Platinum 4", 16:"Platinum 3", 17:"Platinum 2", 17:"Platinum 1", 18:"Diamond 5", 19:"Diamond 4", 20:"Diamond 3", 21:"Diamond 2", 22:"Diamond 1", 23:"Masters", 24:"Challenger"}

wow_ranks = { 0: "Unranked", 1:"<1200", 2:"1200-1600", 3:"1600-1800", 4:"1800-2000", 5:"2000-2200", 6:"2200-2400", 7:"2400-2600", 8:"2600-2800", 9:"2800+"}

def updategetrank(game):
    if game.id == 2:
        return league_ranks
    elif game.id == 3:
        return wow_ranks
    else:
        return no_ranks

def rankify(game, rank):
    if game.id == 2:
        return league_ranks[rank]
    elif game.id == 3:
        return wow_ranks[rank]
    else:
        return no_ranks[rank]



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
    is_premium = models.BooleanField(default=False)
    join_date = models.DateField(auto_now_add=True)
    last_online = models.DateField(auto_now=True)
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
        return self.character.character+" "+self.name.value+" "+self.character.game.name
    

    