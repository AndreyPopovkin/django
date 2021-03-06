from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    deadline = models.DateTimeField(
            blank=True, null=True)
    finished = models.BooleanField()

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title