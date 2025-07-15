from tkinter.constants import CASCADE

from django.db import models
from django.conf import settings

# Create your models here.


class Property(models.Model):

    TYPE_CHOICES = [('rent', 'rent'), ('sale', 'sale')]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField(default=1)
    area = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='rent')
    description = models.TextField()
    image = models.ImageField(upload_to='properties/', blank=True, null=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Properties'


class DealRequest(models.Model):
    STATUSES = (('pending', 'pending'),
                ('approved', 'approved'),
                ('denied', 'denied'))
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )
    seeker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUSES, default='pending')

    def __str__(self):
        return f'Deal Requesst #{self.pk} for {self.property}'

