from django.shortcuts import render, get_object_or_404
from .models import Stream

def add_stream(request):
    stream = Stream()
    stream.streamer = request.auth
    stream.streamkey = request.auth.uprofile.streamkey
    stream.game = request.auth.uprofile.playing_game
    stream.save()

def home(request):
    stream = Stream.objects.all()
    return render(request, "stream/index.html", {"streams":stream})

def get_stream(request, id):
    stream = get_object_or_404(Stream, pk=id)
    return render(request, "stream/stream.html", {"stream":stream})


def get_catagory(request):
    pass