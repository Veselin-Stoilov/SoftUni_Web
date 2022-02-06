from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(
        max_length=15,
    )
    text = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return f'{self.id}: {self.title}: {self.text}'


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )
    type = models.CharField(
        max_length=30,
    )

