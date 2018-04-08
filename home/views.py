from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from games.models import *
from accounts.models import CharacterProfile

def get_index(request):
    return render(request, "home/index.html")
    
def search(request):
    profiles = User.objects.filter(username__icontains=request.GET.get("query"))
    games = Game.objects.filter(name__icontains=request.GET.get("query"))
    publisher = Publisher.objects.filter(name__icontains=request.GET.get("query"))
    characters = CharacterProfile.objects.filter(character__icontains=request.GET.get("query"))
    return render(request, "home/search.html", {'profiles':profiles, 'games':games, 'publisher':publisher, "characters":characters})