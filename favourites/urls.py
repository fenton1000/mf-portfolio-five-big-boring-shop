from django.urls import path
from . import views

urlpatterns = [
    path(
        'add_favourite/<int:product_id>/',
        views.add_favourite,
        name='add_favourite'
    ),
    path(
        'delete_favourite/<product_id>',
        views.delete_favourite,
        name='delete_favourite'
    ),
]
