from django.test import TestCase, Client
from django.urls import reverse
from task_manager.users.models import CustomUsers


class BaseClassTestCase(TestCase):
    def setUp(self):
        self.user = CustomUsers.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')


class RegistrationTestCase(TestCase):
    def test_user_registration(self):
        client = Client()

        response = client.post(reverse('users_register'), {
            'first_name': 'django',
            'last_name': 'test',
            'username': 'testuser',
            'password1': 'testpassword12',
            'password2': 'testpassword12'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            CustomUsers.objects.filter(username='testuser').exists()
        )


class UserProfileUpdateTestCase(BaseClassTestCase):
    def test_user_profile_update(self):
        url = reverse('users_update', kwargs={'pk': self.user.id})

        response = self.client.post(url, {
            'first_name': 'Sasha',
            'last_name': 'Testik',
            'username': 'testuser',
            'password1': 'testpassword12',
            'password2': 'testpassword12'
        })

        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Sasha')
        self.assertEqual(self.user.last_name, 'Testik')


class UserDeletionTestCase(BaseClassTestCase):
    def test_user_deletion(self):
        url = reverse('users_delete', kwargs={'pk': self.user.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            CustomUsers.objects.filter(username='testuser').exists()
        )
