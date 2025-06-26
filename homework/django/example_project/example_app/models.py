from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=250)
    is_bought = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
