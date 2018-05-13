from django.db import models

from accounts.models import *

import datetime

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class Premium(models.Model):
    user = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE, related_name="premium")
    expires = models.DateField(auto_now_add=True)
    express = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{0}".format(self.user)
        
        
    def markPremium(self, time):
        self.expires += time
        self.user.is_premium = True
        self.user.save()
        self.save()
        
        
    def markNormal(self):
        if self.expires < datetime.datetime.now():
            self.user.is_premium = False
            self.user.save()
        self.save()
        
    
    