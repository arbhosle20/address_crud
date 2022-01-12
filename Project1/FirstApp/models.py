from django.db import models


class Address(models.Model):
    flat_no = models.IntegerField()
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    area = models.CharField(max_length=100)
    landmark = models.CharField(max_length=80,blank=True)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

# Create your models here.
