from django.db import models
from django.utils import timezone

class TutorRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    board = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
