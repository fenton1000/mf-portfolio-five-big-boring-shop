from django.urls import path
from . import views

urlpatterns = [
    path(
        'comment_rate_product/<product_id>',
        views.comment_rate_product,
        name='comment_rate_product'
    ),
    path(
        'edit_product_comment_rating/<product_id>',
        views.edit_product_comment_rating,
        name='edit_product_comment_rating'
    ),
    path(
        'delete_product_comment_rating/<product_id>',
        views.delete_product_comment_rating,
        name='delete_product_comment_rating'
    ),
]
