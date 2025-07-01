from django.db import models
from user.models import User

# Create your models here.


class Vacancy(models.Model):

    title = models.CharField(max_length=255)
    offer = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Vacancies'

    