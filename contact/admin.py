from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    readonly_fields = (
        'user_profile',
        'full_name',
        'email',
        'query',
        'date',
    )
    
    list_display = (
        'date',
        'email',
        'viewed',
        'issue_closed',
    )
    ordering = [
        'date',
    ]
