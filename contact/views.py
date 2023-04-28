from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request,
                'Thank you for contacting us! We will get back to you shortly.'
            )
            contact_form = ContactForm()

    context = {
        'form': contact_form
    }

    return render(request, 'contact/contact.html', context)
