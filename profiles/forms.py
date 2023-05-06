from django import forms
from django.utils.translation import gettext_lazy as _
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        labels = {
            "default_phone_number": _("Phone Number"),
            "default_street_address1": _("Address Line 1"),
            "default_street_address2": _("Address Line 2"),
            "default_town_or_city": _("Town/City"),
            "default_town_or_city": _("Town/City"),
            "default_county": _("County"),
            "default_eircode": _("Eircode"),
        }

    def __init__(self, *args, **kwargs):
        """
        Set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
