from django.db import models

# Create your models here.


class Expense(models.Model):
    text = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
