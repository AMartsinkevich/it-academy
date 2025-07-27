from django.db import models
from django.conf import settings


class Contract(models.Model):
    ba_id = models.CharField(max_length=50)
    cs_id = models.CharField(max_length=50)
    co_id = models.CharField(max_length=50)
    co_id_bub = models.CharField(max_length=50)


class Sale(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    device = models.CharField(max_length=100)
    imei = models.CharField(max_length=30)


class Sales(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=250)
    contract = Contract()
    xml = models.CharField(max_length=1000)
    sale = Sale()
