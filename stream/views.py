from django.shortcuts import render, get_object_or_404, redirect
from .models import Stream

def home(request):
    stream = Stream.objects.filter(is_online=True)
    return render(request, "stream/index.html", {"streams":stream})

def get_stream(request, id):
    stream = get_object_or_404(Stream, pk=id)
    return render(request, "stream/stream.html", {"stream":stream})

def go_live(request):
    if request.user.is_authenticated and request.user.uprofile:
        if Stream.objects.filter(streamer=request.user):
            stream = Stream.objects.get(streamer=request.user)
        else:
            stream = Stream()
            stream.streamer = request.user
            stream.streamkey = request.user.uprofile.streamkey
            stream.game = request.user.uprofile.playing_game
        if request.user.uprofile.is_featured:
            stream.featured = True
        if request.user.uprofile.is_premium:
            stream.featured = True
        stream.is_online = True
        stream.save()
        return redirect("home")
    return redirect("home")

def go_offline(request, id):
    stream = Stream.objects.get_object_or_404(pk=id)
    if stream.streamer == request.user:
        stream.is_online = False
        stream.save()
        return redirect("yourprofile")
    else:
        return redirect("streams")
    

def get_catagory(request):
    pass