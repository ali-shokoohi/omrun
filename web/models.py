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
    date = models.DateField()

    def __str__(self):
        return str(self.amount)

class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name

class CommentsOfWeb(models.Model):
    author = models.ForeignKey(Clients, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    date = models.DateField()

    def __str__(self):
        return str(self.author)

class Projects(models.Model):
    name = models.TextField(null=False)
    price = models.BigIntegerField(null=False)
    done = models.BooleanField()
    employer = models.ForeignKey(Employees, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Plans(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    photo = models.ImageField()
    data = models.TextField()
    kind = models.TextField()

    def __str__(self):
        return self.project.name

class Photos(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.project.name

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Photos, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    date = models.DateField()

    def __str__(self):
        return self.author.first_name

class Likes(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Photos, on_delete=models.CASCADE)
    Numbers = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.author.first_name