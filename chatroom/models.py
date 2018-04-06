from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.TextField()

    def __unicode__(self):
        return self.message
        
class PrivateChat(models.Model):
    creator = models.ForeignKey(User, blank=False, related_name="owner")
    allowed = models.ForeignKey(User, blank=False, related_name="other")
    creatorread = models.BooleanField(default=False)
    allowedread = models.BooleanField(default=False)
    
    
    def __unicode__(self):
        return self.creator+" "+self.allowed
    
    def __str__(self):
        return self.creator+" "+self.allowed
        
    def creatorreadfalse(self):
        self.creatorread = False
        print("Setting Creator read False")
        self.save()
        
    def allowreadfalse(self):
        self.allowedread = False
        print("Setting Allowed read False")
        self.save()
    
    def creatorreadTrue(self):
        self.creatorread = True
        print("Setting Creator read True")
        self.save()
        
    def allowreadTrue(self):
        self.allowedread = True
        print("Setting Allowed read True")
        self.save()
        
class PrivateMessage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    chatroom = models.ForeignKey(PrivateChat, related_name="chat_messages")
    user = models.ForeignKey("auth.user")
    message = models.TextField()
    # attached = models.MediaField(blankfjlksdjfl )
    
    def __unicode__(self):
        return self.message
    
        
        
        
        
        
        