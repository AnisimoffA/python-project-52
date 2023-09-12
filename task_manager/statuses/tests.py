from django.test import TestCase, Client
from django.urls import reverse
from task_manager.users.models import CustomUsers
from task_manager.statuses.models import Status


class BaseClassTestCase(TestCase):
    def setUp(self):
        self.user = CustomUsers.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')


class StatusCreateTestCase(BaseClassTestCase):
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


class StatusUpdateTestCase(BaseClassTestCase):
    def test_status_creation(self):
        # Тестирование обновление данных формы
        status = Status.objects.create(name="TestStatus")
        url = reverse('statuses_update', kwargs={'pk': status.id})

        response = self.client.post(url, {
            'name': 'UpdatedName',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='UpdatedName').exists())


class StatusDeletionTestCase(BaseClassTestCase):
    def test_status_deletion(self):
        # Тестирование на удаление из базы данных
        status = Status.objects.create(name="TestStatus")
        url = reverse('statuses_delete', kwargs={'pk': status.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(name='TestStatus').exists())
