from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.utils import timezone

#Modify django user or use this
class User(AbstractUser):
    pass

class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.TextField(null=False)
    profile_pic = models.ImageField(default="default-user.jpg")

    def __str__(self):
        return self.user.first_name

class Purchases(models.Model):
    buyer = models.ForeignKey(Employees, on_delete=models.CASCADE)
    amount = models.BigIntegerField(null=False)
    receipt = models.ImageField(default="default-receipt.jpg")
    name = models.TextField()
    via = models.TextField()
    info = models.TextField(null=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.amount)

class Documents(models.Model):
    name = models.TextField()
    info = models.TextField()
    file = models.FileField(default="default-file.pdf")
    person = models.ForeignKey(Employees, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    subtitle = models.TextField()

    def __str__(self):
        return self.name
    


class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="default-user.jpg")

    def __str__(self):
        return self.user.first_name

class CommentsOfWeb(models.Model):
    author = models.ForeignKey(Clients, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.author)

class Geographical(models.Model):
    location = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "{0}:{1}".format(self.latitude, self.longitude)

class Projects(models.Model):
    name = models.TextField(null=False)
    price = models.BigIntegerField(null=False)
    image = models.ImageField(default="default-project.jpg")
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField()
    geographical = models.ForeignKey(Geographical, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employees, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Plans(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    photo = models.ImageField(default="default-plan.png")
    data = models.TextField()
    kind = models.TextField()

    def __str__(self):
        return self.project.name

class AllowPersons(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Tasks(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    important = models.IntegerField()
    owner = models.ForeignKey(Employees, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    subject = models.TextField()
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.subject

class TasksPerson(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    person = models.ForeignKey(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.person)
    

class ToDo(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    details = models.TextField()
    done = models.BooleanField()

    def __str__(self):
        return self.details

class Gallery(models.Model):
    name = models.TextField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Photos(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField()
    caption = models.TextField()

    def __str__(self):
        return self.project.name

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Photos, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.first_name

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Photos, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name