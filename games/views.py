from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def Home(request):
    games = Game.objects.all()
    return render(request, "games/index.html", {"games":games})
    
def get_game(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, "games/game.html", {"game":game})
    
def get_publisher(request, id):
    publisher = get_object_or_404(Publisher, pk=id)
    print(publisher)
    games = Game.objects.filter(publisher=publisher)
    return render(request, "games/publisher.html", {"publisher" : publisher, "games":games})
    