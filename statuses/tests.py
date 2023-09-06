from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import CustomUsers
from statuses.models import Status


# Create your tests here.
class StatusCreateTestCase(TestCase):
    def setUp(self):
        self.user = CustomUsers.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_with_correct_data(self):
        # Тестирование корректных данных в форме
        url = reverse('statuses_create')

        response = self.client.post(url, {
            'name': 'TestStatus',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='TestStatus').exists())

    def test_with_incorrect_data(self):
        # Тестирование некорректных данных в форме
        url = reverse('statuses_create')

        response = self.client.post(url, {
            'name': '',
        })

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Status.objects.filter(name='').exists())


class StatusUpdateTestCase(TestCase):
    def setUp(self):
        self.user = CustomUsers.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')
        self.status = Status.objects.create(name="TestStatus")

    def test_status_creation(self):
        # Тестирование обновление данных формы
        client = Client()
        url = reverse('statuses_update', kwargs={'pk': self.status.id})

        response = client.post(url, {
            'name': 'UpdatedName',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='UpdatedName').exists())


class StatusDeletionTestCase(TestCase):
    def setUp(self):
        self.user = CustomUsers.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')
        self.status = Status.objects.create(name="TestStatus")

    def test_status_deletion(self):
        # Тестирование на удаление из базы данных
        url = reverse('statuses_delete', kwargs={'pk': self.status.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(name='TestStatus').exists())
