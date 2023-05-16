from django.test import TestCase
from .models import Contact


class TestModels(TestCase):

    def test_viewed_defaults_to_false(self):
        contact = Contact.objects.create(
            full_name='Test User',
            email='test@email.ie',
            query='My query'
        )
        self.assertFalse(contact.viewed)

    def test_issue_closed_defaults_to_false(self):
        contact = Contact.objects.create(
            full_name='Test User',
            email='test@email.ie',
            query='My query'
        )
        self.assertFalse(contact.issue_closed)

    def test_contact_string_method_returns_full_name(self):
        contact = Contact.objects.create(
            full_name='Test User',
            email='test@email.ie',
            query='My query'
        )
        self.assertEqual(str(contact), 'Test User')
