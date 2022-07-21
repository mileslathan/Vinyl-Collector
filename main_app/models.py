from django.db import models
from django.urls import reverse

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    released = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'record_id': self.id})