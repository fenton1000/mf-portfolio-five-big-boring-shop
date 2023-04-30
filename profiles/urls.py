from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
    ),
    path(
        'delete_favourite/<product_id>',
        views.delete_favourite,
        name='delete_favourite'
    ),
    path('rate_product/<product_id>', views.rate_product, name='rate_product'),
    path(
        'edit_product_rating/<product_id>',
        views.edit_product_rating,
        name='edit_product_rating'
    ),
    path(
        'delete_product_rating/<product_id>',
        views.delete_product_rating,
        name='delete_product_rating'
    ),
    path('add_comment/<product_id>', views.add_comment, name='add_comment'),
    path(
        'delete_comment/<comment_id>',
        views.delete_comment,
        name='delete_comment'
        ),
    path('edit_comment/<comment_id>', views.edit_comment, name='edit_comment'),
]
