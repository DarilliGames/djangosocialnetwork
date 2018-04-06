from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import *
from .models import *
from follow.models import Follow

league_ranks = { 0:"Unranked", 1:"Bronze 3 or less", 2:"Bronze 1", 3:"Silver 3", 4:"Silver 1", 5:"Gold 3", 6:"Gold 1", 7:"Platinum 3", 8:"Platinum 1", 9:"Diamond 3", 10:"Diamond 1", 11:"Masters", 12:"Challenger"}


wow_ranks = { 0: "Unranked", 1:"<1200", 2:"1200-1600", 3:"1600-1800", 4:"1800-2000", 5:"2000-2200", 6:"2200-2400", 7:"2400-2600", 8:"2600-2800", 9:"2800+"}

# { 0: "Unranked", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:"", 10:"", 11:"", 12:""}



def get_rank(game, rank):
    if game.id == 1:
        return league_ranks[rank]
    if game.id == 2:
        return wow_ranks[rank]
    else:
        return str(rank)
    
    
    
def get_index(request):
    profiles = User.objects.all()
    return render(request, "accounts/index.html", {"profiles":profiles})
    
def logout(request):
    auth.logout(request)
    url = request.META.get('HTTP_REFERER')
    messages.success(request, "you logged out successfully")
    return HttpResponseRedirect(url)

def login(request):
    for k in request.GET:
        print(request.GET[k])
    redirect_to = request.GET.get('next', 'home')
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            #Authenticate the user
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))
            # if the user is a user, and has correct password
            if user is not None:
                #Log them in
                auth.login(request, user)
                messages.success(request, "You have sucessfully logged out")
                return redirect(redirect_to)
            else:
                # say no
                form.add_error(None, "Your username or password was not recognised")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', { 'form': form })

@login_required()
def yourprofile(request):
    characters = CharacterProfile.objects.filter(userprofile=request.user)
    for c in characters:
        c.rank = get_rank(c.game, c.rank)
    return render(request, 'accounts/yourprofile.html', {"characters":characters})
    
    
def profile(request, id):
    person = get_object_or_404(User, pk=id)
    characters = CharacterProfile.objects.filter(userprofile=person)
    if Follow.objects.filter(follower=request.user, followed=person):
        followstatus = True
    else:
        followstatus = False
    return render(request, 'accounts/profile.html', {"person":person, "followstatus":followstatus, "characters":characters})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('yourprofile')
            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})



@login_required()
def remove_profile(request, id):
    profile = get_object_or_404(User, pk=id)
    if request.user.id == profile.id or request.user.is_staff:
        auth.logout(request)
        profile.delete()
    return redirect('home')


def update_profile(request):
    if request.method=="POST":
        form = ProfileForm(request.POST)
        if request.user.uprofile:
            upro = request.user.uprofile
            upro.bio=request.POST.get('bio')
            upro.streamkey=request.POST.get('streamkey')
            upro.save()
            return redirect("yourprofile")
        if form.is_valid:
            upro = form.save(commit=False)
            upro.user = request.user
            upro.last_online = timezone.now()
            upro.save()
            return render(request, "accounts/update.html", {"form":form})
    
    if request.user.uprofile:
        form = ProfileForm(instance=request.user.uprofile)
    else:
        form = ProfileForm()
    return render(request, "accounts/update.html", {"form":form})

def create_character(request):
    if request.method=="POST":
        form = CharacterProfileForm(request.POST)
        char = form.save(commit=False)
        char.userprofile = request.user
        char.save()
        return redirect("yourprofile")
    else:
        form = CharacterProfileForm()
        return render(request, "accounts/createcharacter.html", {"form":form})