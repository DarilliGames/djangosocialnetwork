from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Follow

def follow_user(request, id):
    followeduser = get_object_or_404(User, pk=id)
    follower = request.user
    if followeduser != follower:
        f = Follow()
        f.followed = followeduser
        f.follower = follower
        f.save()
    else:
        print("you can not follow yourself!")
        return redirect('profile', id)
    return redirect('profile', id)
    

def unfollow_user(request, id):
    followeduser = get_object_or_404(User, pk=id)
    follow = Follow.objects.filter(followed=followeduser, follower=request.user)
    follow.delete()
    return redirect('profile', id)