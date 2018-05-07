from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from games.models import *
from accounts.models import *

def get_index(request):
    featured = []
    for x in UserProfile.objects.all():
        if x.is_featured:
            featured.append(x)
            
    games = Game.objects.all().order_by('-reviews_score')
    ngames = Game.objects.all().order_by('-release_date')
    newgame = ngames[0]
    
    fgames = [games[0], games[1]]
        
    return render(request, "home/index.html", {"featured":featured, "games":games, "newgame":newgame, "fgames":fgames})
    
    
def progress(request):
    
    return render(request, "home/progress.html")
    
