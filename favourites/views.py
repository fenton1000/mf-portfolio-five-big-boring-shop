from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Favourites

from products.models import Product


@login_required
def add_favourite(request, product_id):
    """ Add a product to user favourite list """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    if Favourites.objects.filter(
        user=user,
        product=product,
    ).exists():
        messages.warning(request, 'This product was already on your list!')
    else:
        Favourites.objects.create(
            user=user,
            product=product,
        )
        messages.success(request, 'Product added to Favourites!')
    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def delete_favourite(request, product_id):
    """ Delete a product from user favourite list """

    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    favourite = get_object_or_404(Favourites, user=user, product=product)
    favourite.delete()
    messages.success(request, 'Product deleted from favourites!')
    return redirect('profile')
