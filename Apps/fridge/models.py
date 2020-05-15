from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Fridge(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fridge-detail', kwargs={'pk': self.pk})


class Recipe(models.Model):
    pass
