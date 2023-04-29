from django.contrib import admin

from .models import UserProfile, Favourites, Rating

admin.site.register(UserProfile)
admin.site.register(Favourites)
admin.site.register(Rating)
