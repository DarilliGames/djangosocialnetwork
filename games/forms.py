from django import forms
from .models import *
        
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'blurb', 'bio', 'contact', 'img_logo')
        
 

    
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'publisher', 'blurb', 'bio', 'img_thumbnail', 'img_tall')
