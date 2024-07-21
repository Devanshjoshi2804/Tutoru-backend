from django.db import models

class TutorRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    board = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
