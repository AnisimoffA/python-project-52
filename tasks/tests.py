from django.test import TestCase, Client
from django.urls import reverse
from users.models import *
from statuses.models import *
from tasks.models import *
from labels.models import *
# Create your tests here.


class BaseTestClass(TestCase):
    def setUp(self):
        self.user = CustomUsers.objects.create_user(username='test_user', password='test_password')
        self.client = Client()
        self.client.login(username='test_user', password='test_password')


class TaskCreateTestCase(BaseTestClass):
    def test_with_correct_data(self):
        # Тестирование корректных данных в форме
        status = Status.objects.create(name='test_status')
        url = reverse('task_create')
        data = {
            'name': 'test_task',
            'status': status.id,
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='test_task').exists())

    def test_with_incorrect_data(self):
        # Тестирование некорректных данных в форме
        url = reverse('statuses_create')
        updated_data = {'name': ''}

        response = self.client.post(url, updated_data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Status.objects.filter(name='').exists())


class TaskUpdateTestCase(BaseTestClass):
    def test_status_creation(self):
        # Тестирование обновление данных формы
        status = Status.objects.create(name='test_status')
        task = Task.objects.create(creator=self.user, name='test_task', status=status)
        url = reverse('task_update', kwargs={'pk': task.pk})
        updated_data = {
            'name': 'new_data',
            'description': 'new_description',
            'status': status.id
            }

        response = self.client.post(url, updated_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='new_data').exists())


class TaskDeletionTestCase(BaseTestClass):
    def test_status_deletion(self):
        # Тестирование на удаление из базы данных
        status = Status.objects.create(name='test_status')
        task = Task.objects.create(creator=self.user, name='test_task', status=status)
        url = reverse('task_delete', kwargs={'pk': task.id})

        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(name='test_task').exists())


class TaskFilterTestCase(TestCase):
    def setUp(self):
        self.user = CustomUsers.objects.create_user(username='test_user', password='test_password')
        self.client = Client()
        self.client.login(username='test_user', password='test_password')

        self.status = Status.objects.create(name='test_status')
        self.executor = CustomUsers.objects.create_user(username='test_executor', password='test_password')
        self.label = Label.objects.create(name="test_label")
        self.task = Task.objects.create(creator=self.user, name='test_task2', executor=self.executor, status=self.status)
        self.task.labels.set(Label.objects.filter(name="test_label"))

        self.url = reverse('task_list')

    def test_status_filter(self):
        data = {
            'status': self.status.id
        }

        response = self.client.get(self.url, data)

        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.status)
        self.assertContains(response, self.task.executor)

    def test_executor_filter(self):

        data = {
            'executor': self.executor.id
        }

        response = self.client.get(self.url, data)

        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.status)
        self.assertContains(response, self.task.executor)

    def test_labels_filter(self):
        data = {
            'label': self.label.id
        }

        response = self.client.get(self.url, data)

        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.status)
        self.assertContains(response, self.task.executor)

    def test_creator_filter(self):
        data = {
            'show_my_articles': True
        }

        response = self.client.get(self.url, data)

        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.status)
        self.assertContains(response, self.task.executor)
