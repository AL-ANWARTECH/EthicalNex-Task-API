from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task
from datetime import timedelta, datetime, time
from django.utils import timezone
from django.urls import reverse
from rest_framework_simplejwt.tokens import AccessToken


class TaskAPITestCase(TestCase):

    def setUp(self):
        # Set up a test user and authenticate
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Obtain JWT token for authentication
        self.token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Create precise test data with timezone-aware datetimes
        now = timezone.now()
        self.today = now.date()
        
        # Create tasks with explicit due dates at noon
        self.task_today = Task.objects.create(
            user=self.user,
            title="Today's Task",
            due_date=timezone.make_aware(datetime.combine(self.today, time(12, 0))),
            completed=False
        )
        self.task_tomorrow = Task.objects.create(
            user=self.user,
            title="Tomorrow's Task",
            due_date=timezone.make_aware(datetime.combine(self.today + timedelta(days=1), time(12, 0))),
            completed=True
        )
        self.task_future = Task.objects.create(
            user=self.user,
            title="Future Task",
            due_date=timezone.make_aware(datetime.combine(self.today + timedelta(days=2), time(12, 0))),
            completed=False
        )

    def test_create_task(self):
        data = {
            'title': 'New Task',
            'description': 'Description for new task',
            'completed': False,
            'due_date': (timezone.now() + timedelta(days=5)).isoformat()
        }
        response = self.client.post(reverse('tasks:task-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Task')

    def test_filter_completed_tasks(self):
        response = self.client.get(reverse('tasks:task-list') + '?completed=true', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Tomorrow's Task")

    def test_filter_incomplete_tasks(self):
        response = self.client.get(reverse('tasks:task-list') + '?completed=false', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        titles = {task['title'] for task in response.data}
        self.assertEqual(titles, {"Today's Task", "Future Task"})

    def test_filter_tasks_by_due_date(self):
        # Test exact date match
        today_str = self.today.isoformat()
        response = self.client.get(f"{reverse('tasks:task-list')}?due_date={today_str}", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.task_today.id)

    def test_filter_tasks_by_date_range(self):
        # Test date range (greater than today)
        today_str = self.today.isoformat()
        response = self.client.get(f"{reverse('tasks:task-list')}?due_date__gt={today_str}", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        returned_ids = {task['id'] for task in response.data}
        self.assertEqual(returned_ids, {self.task_tomorrow.id, self.task_future.id})

    def test_search_task_by_title(self):
        response = self.client.get(reverse('tasks:task-list') + '?search=Tomorrow', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Tomorrow's Task")

    def test_order_tasks_by_due_date(self):
        response = self.client.get(reverse('tasks:task-list') + '?ordering=due_date', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['title'], "Today's Task")
        self.assertEqual(response.data[1]['title'], "Tomorrow's Task")
        self.assertEqual(response.data[2]['title'], "Future Task")

    def test_task_detail(self):
        response = self.client.get(reverse('tasks:task-detail', args=[self.task_today.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Today's Task")

    def test_task_update(self):
        data = {'title': 'Updated Today Task', 'completed': True}
        response = self.client.put(
            reverse('tasks:task-detail', args=[self.task_today.id]),
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Today Task')
        self.assertTrue(response.data['completed'])

    def test_task_delete(self):
        response = self.client.delete(
            reverse('tasks:task-detail', args=[self.task_today.id]),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task_today.id).exists())