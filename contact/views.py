from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """

    message_sent = None
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            if request.user.is_authenticated:
                contact.user_profile = request.user.userprofile
            contact.save()
            messages.success(
                request,
                'Thank you for contacting us! We will get back to you shortly.'
            )
            message_sent = contact
            contact_form = ContactForm()
    else:
        contact_form = ContactForm()
        if request.user.is_authenticated:
            contact = contact_form.save(commit=False)
            contact.full_name = request.user.get_full_name()
            contact.email = request.user.email
            contact_form = ContactForm(instance=contact)

    context = {
        'form': contact_form,
        'message_sent': message_sent
    }

    return render(request, 'contact/contact.html', context)
