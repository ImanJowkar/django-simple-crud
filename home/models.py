from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created = models.DateTimeField()   