from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import CustomUsers
from labels.models import Label
# Create your tests here.


class BaseTestClass(TestCase):
    def setUp(self):
        self.user = CustomUsers.objects.create_user(username='test_user', password='test_password')
        self.client = Client()
        self.client.login(username='test_user', password='test_password')


class LabelCreateTestCase(BaseTestClass):
    def test_with_correct_data(self):
        # Тестирование корректных данных в форме
        url = reverse('label_create')

        response = self.client.post(url, {
            'name': 'TestLabel',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name='TestLabel').exists())

    def test_with_incorrect_data(self):
        # Тестирование некорректных данных в форме
        url = reverse('label_create')

        response = self.client.post(url, {
            'name': '',
        })

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Label.objects.filter(name='').exists())


class LabelUpdateTestCase(BaseTestClass):
    def test_status_creation(self):
        # Тестирование обновление данных формы
        label = Label.objects.create(name="TestLabel")
        url = reverse('label_update', kwargs={'pk': label.id})

        response = self.client.post(url, {
            'name': 'UpdatedName',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name='UpdatedName').exists())


class LabelDeletionTestCase(BaseTestClass):
    def test_status_deletion(self):
        # Тестирование на удаление из базы данных
        label = Label.objects.create(name="TestLabel")
        url = reverse('label_delete', kwargs={'pk': label.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Label.objects.filter(name='TestLabel').exists())
