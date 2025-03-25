from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import timezone

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  # Ensure timezone-aware datetime

    def __str__(self):
        return self.title
