import json
from django.shortcuts import render
from accounts.models import *
from games.models import *

league_ranks = { 0:"Unranked", 1:"Bronze 3 or less", 2:"Bronze 1", 3:"Silver 3", 4:"Silver 1", 5:"Gold 3", 6:"Gold 1", 7:"Platinum 3", 8:"Platinum 1", 9:"Diamond 3", 10:"Diamond 1", 11:"Masters", 12:"Challenger"}

wow_ranks = { 0: "Unranked", 1:"<1200", 2:"1200-1600", 3:"1600-1800", 4:"1800-2000", 5:"2000-2200", 6:"2200-2400", 7:"2400-2600", 8:"2600-2800", 9:"2800+"}

# { 0: "Unranked", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:"", 10:"", 11:"", 12:""}



def get_rank(game, rank):
    if game.id == 1:
        return league_ranks[rank]
    if game.id == 3:
        return wow_ranks[rank]
    else:
        return str(rank)
    

def search(request):
    profiles = User.objects.filter(username__icontains=request.GET.get("query"))
    games = Game.objects.filter(name__icontains=request.GET.get("query"))
    publisher = Publisher.objects.filter(name__icontains=request.GET.get("query"))
    characters = CharacterProfile.objects.filter(character__icontains=request.GET.get("query"))
    return render(request, "search/search.html", {'profiles':profiles, 'games':games, 'publisher':publisher, "characters":characters})


def search_games(request):
    if request.method=="POST":
        pass
    return render(request, "search/games.html")


def search_users(request):
    pass    


def search_characters(request):
    if request.method=="POST":
        results = []
        game = Game.objects.get(name=request.POST.get("gamequery"))
        print(game)
        characters = CharacterProfile.objects.filter(character__icontains=request.POST.get("query"))

        for c in characters:
            print(c.game.name)
            if c.game.name == game.name:
                c.rank = get_rank(c.game, c.rank)
                results.append(c)
                
        return render(request, "search/charactersearch.html", {"characters":results})
    games=Game.objects.all()
    gameslist = []
    for g in games:
        gameslist.append(g.name)
    
    return render(request, "search/charactersearch.html", {"games":gameslist})
    