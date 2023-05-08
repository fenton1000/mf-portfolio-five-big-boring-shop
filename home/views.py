from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def thanks(request):
    """
    A view to return the index page with a
    mailchimp subscription confirmation message
    """

    messages.success(request, 'Thank you for subscribing!')

    return redirect('home')
