from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    released = models.IntegerField()
    country = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'record_id': self.id})