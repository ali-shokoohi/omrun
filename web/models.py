from django.db import models

class Employees(models.Model):
    name = models.TextField(null=False)
    post = models.TextField(null=False)
    personnelـid = models.BigIntegerField(null=False, primary_key=True)
    password = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=32)
    profile_pic = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Purchases(models.Model):
    buyer = models.ForeignKey(Employees, on_delete=models.CASCADE)
    amount = models.BigIntegerField(null=False)
    for_what = models.TextField(null=False)
    date = models.TextField()

    def __str__(self):
        return str(self.amount)
