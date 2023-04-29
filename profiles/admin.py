from django.contrib import admin

from .models import UserProfile, Favourites, Rating, Comment

admin.site.register(UserProfile)
admin.site.register(Favourites)
admin.site.register(Rating)
admin.site.register(Comment)
