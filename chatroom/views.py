from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *

def Home(request):
    c = Chat.objects.all()
    return render(request, "chatroom/home.html", {'home': 'active', 'chat': c})

def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        msg = c.user.username+": "+msg
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username})
    else:
        return HttpResponse('Request must be POST.')

def Messages(request):
    chat = Chat.objects.all()
    return render(request, 'chatroom/messages.html', {'chat' : chat})

@login_required()
def PGet(request, id):
    recipient = get_object_or_404(User, pk=id)
    if PrivateChat.objects.filter(creator=recipient, allowed=request.user):
        proom = get_object_or_404(PrivateChat, creator=recipient, allowed=request.user)
        proom.allowreadTrue()
        proom.save()
        return redirect(reverse('pchat', args=(proom.id,)))
    elif PrivateChat.objects.filter(creator=request.user, allowed=recipient):
        proom = get_object_or_404(PrivateChat, creator=request.user, allowed=recipient)
        proom.creatorreadTrue()
        proom.save()
        return redirect(reverse('pchat', args=(proom.id,)))
    else:
        proom = PrivateChat(creator=request.user, allowed=recipient)
        proom.save()
        return redirect(reverse('pchat', args=(proom.id,)))

@login_required()
def PChat(request, id):
    proom = get_object_or_404(PrivateChat, pk=id)
    if request.user == proom.creator or request.user == proom.allowed:
        pchat = PrivateMessage.objects.filter(chatroom=id)
        if request.user == proom.creator:
            proom.creatorreadTrue()
        if request.user == proom.allowed:
            proom.creatorreadTrue()
        return render(request, "chatroom/chat.html", {'chat' : pchat, "proom":proom})
    else:
        return redirect("chat")

def PMessages(request, id):
    chat = PrivateMessage.objects.filter(chatroom=id)
    return render(request, 'chatroom/messages.html', {'chat' : chat})
    
def PPost(request, id):
    chatroom = get_object_or_404(PrivateChat, pk=id)
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = PrivateMessage(user=request.user, message=msg)
        msg = c.user.username+": "+msg
        c = PrivateMessage(user=request.user, message=msg)
        if msg != '':
            c.chatroom = chatroom
            c.save()
            if c.user == chatroom.creator:
                chatroom.allowreadfalse()
                chatroom.creatorreadTrue()
            if c.user == chatroom.allowed:
                chatroom.creatorreadfalse()
                chatroom.allowreadTrue()
        return JsonResponse({ 'msg': msg, 'user': c.user.username})
    else:
        return HttpResponse('Request must be POST.')