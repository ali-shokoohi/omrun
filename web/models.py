from django.db import models

class Employees(models.Model):
    name = models.TextField(null=False)
    personnelـid = models.BigIntegerField(max_length=16, null=False, primary_key=True)
    password = models.CharField(max_lenght=32, null=False)
    email = models.CharField(max_lenght=32)

    def __str__(self):
        return self.name

class Purchases(models.Model):
    amount = models.BigIntegerField(null=False)
    for_what = models.TextField(null=False)
    date = models.TextField()

    def __str__(self):
        return self.amount