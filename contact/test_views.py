from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username='testuser',
            password='56723dE%',
            first_name='Test',
            last_name='User',
            email='test@email.ie'
        )

    def test_get_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_get_contact_page_with_user_logged_in(self):
        user = self.user
        self.client.force_login(user)
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_can_submit_query(self):
        response = self.client.post(
            '/contact/',
            {
                'full_name': 'Test User',
                'email': 'email@email.ie',
                'query': 'This is a test query'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_can_submit_query_with_user_logged_in(self):
        user = self.user
        self.client.force_login(user)
        response = self.client.post(
            '/contact/',
            {
                'query': 'This is a test query'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
