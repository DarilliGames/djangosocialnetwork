from django.db import models
from django.contrib.auth.models import User

class Publisher(models.Model):
    publisheradmin = models.ForeignKey(User)
    name = models.CharField(max_length=140, blank=False)
    blurb = models.TextField(max_length=140, blank=True)
    bio = models.TextField(max_length=800, blank=True)
    contact = models.CharField(blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    validated = models.BooleanField(default=False)
    img_logo = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.name

class Game(models.Model):
    publisher = models.ForeignKey(Publisher)
    name = models.CharField(max_length=140, blank=False)
    blurb = models.TextField(max_length=140, blank=True)
    bio = models.TextField(max_length=800, blank=True)
    release_date = models.DateTimeField(auto_now_add=True)
    img_thumbnail = models.ImageField(blank=True, upload_to='images')
    img_tall = models.ImageField(blank=True, upload_to='images')
    reviews_num = models.IntegerField(default=0)
    reviews_score = models.IntegerField(default=0)
    
    @property
    def average_rating(self):
        if self.reviews_num < 1:
            return 0
        else:
            return self.reviews_score / self.reviews_num
    
    def __str__(self):
        return self.name
