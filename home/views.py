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
    
        
    return render(request, "home/index.html", {"featured":featured, "games":games})
    
    
def progress(request):
    
    return render(request, "home/progress.html")
    
