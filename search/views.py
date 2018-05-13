import json
from django.shortcuts import render, get_object_or_404
from accounts.models import *
from games.models import *

def search(request):
    profiles = User.objects.filter(username__icontains=request.GET.get("query"))
    premium = []
    for p in profiles:
        if p.uprofile.is_premium:
            premium.append(p)
    games = Game.objects.filter(name__icontains=request.GET.get("query"))
    publisher = Publisher.objects.filter(name__icontains=request.GET.get("query"))
    characters = CharacterProfile.objects.filter(character__icontains=request.GET.get("query"))
    return render(request, "search/search.html", {'premium':premium, 'profiles':profiles, 'games':games, 'publisher':publisher, "characters":characters})

def search_games(request):
    gameslist = []
    games = Game.objects.all()
    for g in games:
        gameslist.append(g.name)
       
    if request.method=="POST":
        games = Game.objects.filter(name__icontains=request.POST.get("query"))
    else:
        games = Game.objects.all()
    return render(request, "search/games.html", {"games":games, "gameslist":gameslist})




def search_users(request):
    if request.method=="POST":
        users = User.objects.filter(username__icontains=request.POST.get("query"))
                
            
        return render(request, "search/searchusers.html", {"users":users})
    
    return render(request, "search/searchusers.html")
    
    
    
def search_characters(request, id):
    game=get_object_or_404(Game, pk=id)
    ranks = updategetrank(game)
    attribute=Attributes.objects.filter(game=game)
    if request.method=="POST":
        name_search = request.POST.get("query")
        if name_search != "":
            characters = CharacterProfile.objects.filter(game=game, character__icontains=request.POST.get("query"))
        else:
            print("YOU HAVE NNNOOOOOO NAME")
            characters = CharacterProfile.objects.filter(game=game)
        search_for = []
        values=[]
        results = []
        for r in attribute:
            search_for.append(r.name)
        for f in search_for:
            a = request.POST.get(f)
            if a != "":
                values.append(int(a))
        results=characters
        
        
        if len(values) == 0:
            pass
        
        else:
            results = CharacterProfile.objects.filter(abouts__name__id__in=values)
            data = []
            for v in values:
                data.append(str(v))
            for f in data:
                g=str(f)
                res=CharacterProfile.objects.filter(abouts__name__id__in=g)
                results = results.intersection(res)
            
                
        return render(request, "search/searchcharacter.html", {"game":game, "characters":results, "attribute":attribute, "ranks":ranks})




    return render(request, "search/searchcharacter.html", {"game":game, "attribute":attribute, "ranks":ranks})
    
    
    
    
    
    