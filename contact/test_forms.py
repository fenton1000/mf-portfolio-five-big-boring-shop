from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_full_name_is_required(self):
        form = ContactForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.'
        )

    def test_email_is_required(self):
        form = ContactForm(
            {
                'full_name': 'Test',
                'email': ''
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_query_is_required(self):
        form = ContactForm(
            {
                'full_name': 'Test',
                'email': 'test@email.ie',
                'query': ''
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn('query', form.errors.keys())
        self.assertEqual(form.errors['query'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ContactForm()
        self.assertEqual(form.Meta.fields, ['full_name', 'email', 'query'])
