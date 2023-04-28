from django.contrib import admin

from .models import UserProfile, Favourites

admin.site.register(UserProfile)
admin.site.register(Favourites)
