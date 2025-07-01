from django.db import models

# Create your models here.


class User(models.Model):

    TYPE_CHOICES = [('reader', 'reader'), ('writer', 'writer')]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='reader')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Users'
