from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Follow(models.Model):
      followed = models.ForeignKey(User, related_name="followby")
      follower = models.ForeignKey(User, related_name="follows")
      follow_time = models.DateTimeField(auto_now=True)
      
      def __str__(self):
          return self.follower.username +" "+ self.followed.username