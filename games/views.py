from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
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
    
    
def add_game(request):
    if request.method=="POST":
        form = GameForm(request.POST)
        game = form.save(commit=False)
        game.save()
        return redirect("yourprofile")

    gameform = GameForm()
    return render(request, "games/createnew.html", {"gameform":gameform})