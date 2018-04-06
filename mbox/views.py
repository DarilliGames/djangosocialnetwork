from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from .models import Mail
from .forms import MailForm

def get_inbox(request):
    return render(request, "mbox/inbox.html")

def get_sent(request):
    return render(request, "mbox/sent.html")

@login_required(login_url='login')
def get_mail(request, id):
    mail = get_object_or_404(Mail, pk=id)
    if (request.user == mail.sender):
        return render(request, "mbox/mail.html", {"mail" : mail})
    elif (request.user == mail.recipient):
        return render(request, "mbox/mail.html", {"mail" : mail})
    else:
        return redirect("index")

def write_mail(request):
    form = MailForm()
    return render(request, "mbox/compose.html", {"form" : form})

def send(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            mail = form.save(commit=False)
            mail.sender = request.user
            mail.save()
    return redirect("inbox")