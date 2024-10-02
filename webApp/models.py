from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Token = models.CharField(max_length=32)


class Expense(models.Model):
    text = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Income(models.Model):
    text = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
