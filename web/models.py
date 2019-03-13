from django.db import models
from django.contrib.auth.models import AbstractUser

#Modify django user or use this
class User(AbstractUser):
    pass

class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.TextField(null=False)
    profile_pic = models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name

class Purchases(models.Model):
    buyer = models.ForeignKey(Employees, on_delete=models.CASCADE)
    amount = models.BigIntegerField(null=False)
    for_what = models.TextField(null=False)
    date = models.TextField()

    def __str__(self):
        return str(self.amount)

class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name

class Comments(models.Model):
    author = models.ForeignKey(Clients, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    date = models.TextField()

    def __str__(self):
        return str(self.author)

class Projects:
    name = models.TextField(null=False)
    employer = models.OneToOneField(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Plans:
    project = models.OneToOneField(Projects, on_delete=models.CASCADE)
    photo = models.ImageField()
    data = models.TextField()
    kind = models.TextField()

    def __str__(self):
        return self.project.name