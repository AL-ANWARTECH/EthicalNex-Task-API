from django_filters.rest_framework import DjangoFilterBackend, DateFilter
import django_filters
from rest_framework import generics, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from django.utils import timezone
from datetime import datetime, time
from datetime import timedelta


class TaskFilter(django_filters.FilterSet):
    # Exact date match filter
    due_date = DateFilter(
        field_name='due_date',
        method='filter_exact_date'
    )
    
    # Date range filters
    due_date__gt = DateFilter(
        field_name='due_date',
        method='filter_date_gt'
    )
    due_date__lt = DateFilter(
        field_name='due_date',
        method='filter_date_lt'
    )

    def filter_exact_date(self, queryset, name, value):
        """Filter for tasks due on exactly this date"""
        return queryset.filter(
            due_date__date=value
        )

    def filter_date_gt(self, queryset, name, value):
        """Filter for tasks due after this date (inclusive of the day after)"""
        next_day = value + timedelta(days=1)
        return queryset.filter(
            due_date__date__gte=next_day
        )

    def filter_date_lt(self, queryset, name, value):
        """Filter for tasks due before this date (exclusive)"""
        return queryset.filter(
            due_date__date__lt=value
        )

    class Meta:
        model = Task
        fields = ['completed']

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TaskFilter
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_at']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('due_date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)