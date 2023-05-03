from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Rating(models.Model):
    """
    Model for saving authenticated users' product ratings
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    user_rating = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    """
    Model for saving authenticated users' product comments
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.user.username
