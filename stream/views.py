from django.shortcuts import render, get_object_or_404
from .models import Stream

def home(request):
    stream = Stream.objects.all()
    return render(request, "stream/index.html", {"streams":stream})

def get_stream(request, id):
    stream = get_object_or_404(Stream, pk=id)
    return render(request, "stream/stream.html", {"stream":stream})


def get_catagory(request):
    pass