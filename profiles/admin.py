from django.contrib import admin

from .models import UserProfile, Rating, Comment

admin.site.register(UserProfile)
admin.site.register(Rating)
admin.site.register(Comment)
