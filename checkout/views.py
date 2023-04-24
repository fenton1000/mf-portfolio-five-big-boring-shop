from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty')
        return redirect('products')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    stripe_public_key = (
        'pk_test_51N0Mk3AcCvg3bp3PZzSy'
        'TC34W67yYOqCAkUoK10lTDe8R9ChHR'
        'ZL1ZP7YXZ0FbCjtLKnf7r2eLqBE'
        'XjkiiSbtqM600DGjYYt1w'
    )
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
