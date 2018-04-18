from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from games.models import Game
from .models import GameReview
from .forms import GameReviewForm
# Create your views here.

@login_required()
def review_game(request, id):
    if request.method == "POST":
        score = int(request.POST.get("score"))
        item = get_object_or_404(Game, pk=id)
        item.reviews_score += score
        item.reviews_num += 1
        item.save()
        form = GameReviewForm(request.POST)
        if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.item = item
                post.rating = score
                post.save()
        return redirect('game', id)
    else:
        return redirect('game', id)