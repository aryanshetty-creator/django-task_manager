from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)  # Task title
    description = models.TextField(blank=True, null=True)  # Optional description
    completed = models.BooleanField(default=False)  # Mark as completed or not
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return self.title

