from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'date',
        'email',
        'viewed',
        'issue_closed',
    )
    ordering = [
        'date',
    ]
