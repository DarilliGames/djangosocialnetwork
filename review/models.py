from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from games.models import Game

# Create your models here.
class GameReview(models.Model):
    author = models.ForeignKey('auth.User')
    item = models.ForeignKey(Game, blank=False)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=400)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(0),
        MaxValueValidator(5)])
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        