import json
from django.shortcuts import render, get_object_or_404
from accounts.models import *
from games.models import *

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
    games=Game.objects.all()
    gameslist = []
    for g in games:
        gameslist.append(g.name)
    if request.method=="POST":
        results = []
        game = Game.objects.get(name=request.POST.get("gamequery"))
        characters = CharacterProfile.objects.filter(character__icontains=request.POST.get("query"))
        for c in characters:
            if game != "" or game != None:
                if c.game.name == game.name:
                    results.append(c)
            else:
                results.append(c)
                
            
        return render(request, "search/searchusers.html", {"characters":results, "games":gameslist})
    
    return render(request, "search/searchusers.html", {"games":gameslist})
    
    
    
def search_characters(request, id):
    game=get_object_or_404(Game, pk=id)
    attribute=Attributes.objects.filter(game=game)
    
    
    if request.method=="POST":
        name_search = request.POST.get("query")
        if name_search != "":
            characters = CharacterProfile.objects.filter(character__icontains=request.POST.get("query"))
        else:
            print("YOU HAVE NNNOOOOOO NAME")
            characters = CharacterProfile.objects.all()
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
            
            print(search_for)
            print(values)
        else:
            results = CharacterProfile.objects.filter(abouts__name__id__in=values)
            data = []
            for v in values:
                data.append(str(v))
            for f in data:
                g=str(f)
                res=CharacterProfile.objects.filter(abouts__name__id__in=g)
                results = results.intersection(res)
            
                
        return render(request, "search/searchcharacter.html", {"game":game, "characters":results, "attribute":attribute})




    return render(request, "search/searchcharacter.html", {"game":game, "attribute":attribute})
    
    
    
    
    
    