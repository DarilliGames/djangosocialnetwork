from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from review.forms import GameReviewForm

def Home(request):
    games = Game.objects.all()
    return render(request, "games/index.html", {"games":games})
    
def get_game(request, id):
    game = get_object_or_404(Game, pk=id)
    form = GameReviewForm()
    return render(request, "games/game.html", {"game":game, "form":form})
    
def get_publisher(request, id):
    publisher = get_object_or_404(Publisher, pk=id)
    games = Game.objects.filter(publisher=publisher)
    return render(request, "games/publisher.html", {"publisher" : publisher, "games":games})

@login_required()
def add_game(request):
    if request.method=="POST":
        form = GameForm(request.POST)
        game = form.save(commit=False)
        game.save()
        return redirect("yourprofile")
    gameform = GameForm()
    return render(request, "games/createnew.html", {"gameform":gameform})

@login_required()
def add_publisher(request):
    if request.method=="POST":
        form = PublisherForm(request.POST)
        game = form.save(commit=False)
        game.publisheradmin = request.user
        game.save()
        return redirect("yourprofile")
    gameform = PublisherForm()
    return render(request, "games/createnew.html", {"gameform":gameform})