from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from accounts.models import UserProfile
from datetime import datetime, timedelta
from .forms import *
from .models import *
import stripe



stripe.api_key = settings.STRIPE_SECRET

def checkout(request):
    order_form = OrderForm()
    payment_form = MakePaymentForm()
    return render(request, "premium/premium.html", {"order_form":order_form, "payment_form":payment_form, "publishable": settings.STRIPE_PUBLISH})

def process(request):
    if request.method =="POST":
        form = OrderForm(request.POST)
        order = form.save()
        total = 5
        pform = MakePaymentForm(request.POST)
        if pform.is_valid():
            if request.user.is_authenticated:
                mail = request.user.email
            try:
                customer = stripe.Charge.create(
                    amount= int(total * 100),
                    currency="EUR",
                    description=mail,
                    card=pform.cleaned_data['stripe_id'],
                    )
                    
                if customer.paid:
                    messages.success(request, "You have sucessfully logged out")
                    print("Paid")
                    puser = request.user.uprofile
                    if Premium.objects.filter(user=request.user.uprofile):
                        pre= Premium.objects.get(user=request.user.uprofile)
                        pre.markPremium(timedelta(days=30))
                        
                    else:
                        pre = Premium(user=puser)
                        pre.save()
                        pre.markPremium(timedelta(days=30))
                    puser.save()
                    return redirect('home')
                    
            except stripe.error.CardError:
                messages.error(request, "Card Invalid")
                print("Invalid")
    
                
        else:
            messages.error(request, "No")
            print("Card Not Valid")
        
        payment_form = MakePaymentForm(request.POST)
        order_form = OrderForm(request.POST)
        
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "premium/premium.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISH })