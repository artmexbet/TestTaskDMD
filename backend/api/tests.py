from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Task


class TaskAPITestCase(TestCase):
    def setUp(self):
        # Создаем клиент для работы с API и тестовые данные
        self.client = APIClient()
        self.task1 = Task.objects.create(name='Task 1',
                                         description='Description 1',
                                         performers='Test performer',
                                         planned_effort='10:15',
                                         actual_effort='10:30')
        self.task2 = Task.objects.create(name='Task 2',
                                         description='Description 2',
                                         performers='Test performer 2',
                                         planned_effort='10:15',
                                         actual_effort='10:30')

    def test_get_tasks(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_task(self):
        data = {
            "name": "Task 3",
            "description": "Description 3",
            "performers": "Test performer",
            "planned_effort": "10:15",
            "actual_effort": "10:30",
        }
        response = self.client.post('/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)

    def test_update_task(self):
        data = {
            "name": "Task 3",
            "description": "Description 3",
            "performers": "Test performer",
            "planned_effort": "10:15",
            "actual_effort": "10:30",
        }
        response = self.client.put(f'/tasks/{self.task1.pk}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.name, 'Task 3')

    def test_delete_task(self):
        response = self.client.delete(f'/tasks/{self.task1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)


class TaskAPINegativeTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task1 = Task.objects.create(name='Task 1', description='Description 1')

    def test_create_task_without_data(self):
        response = self.client.post('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_nonexistent_task(self):
        response = self.client.delete('/tasks/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
