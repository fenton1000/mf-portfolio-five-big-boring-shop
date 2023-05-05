from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class CommentRating(models.Model):
    """
    Model for saving authenticated users'
    product ratings and comments
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user_rating = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.user.username
