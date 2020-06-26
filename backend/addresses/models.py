from django.conf import settings
from django.db import models


class BuyerAddress(models.Model):
    "Generated Model"
    houseNumber = models.BigIntegerField()
    streetName = models.TextField()


# Create your models here.
