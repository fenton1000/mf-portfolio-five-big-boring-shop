from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Favourites(models.Model):
    """
    Model for saving authenticated users' product favourites lists
    """

    class Meta:
        verbose_name_plural = 'Favourites'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favourites'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='favourites'
    )

    def __str__(self):
        return self.user.username
