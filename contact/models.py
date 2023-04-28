from django.db import models

from profiles.models import UserProfile


class Contact(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='contact')
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    email = models.EmailField(max_length=254, null=False, blank=False)
    query = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)
    issue_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name