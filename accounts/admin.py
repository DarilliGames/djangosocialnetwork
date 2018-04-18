from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(CharacterProfile)
admin.site.register(AttributeValue)
admin.site.register(Attributes)
admin.site.register(AttributeChoices)