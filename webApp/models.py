from django.db import models

# Create your models here.


class Expense(models.Model):
    text = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.BigIntegerField()

    def __str__(self):
        return "{}:{}-{}-{}".format(self.text, self.date.year, self.date.month, self.date.day)


class Income(models.Model):
    text = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.BigIntegerField()

    def __str__(self):
        return "{}:{}".format(self.text, self.date)
