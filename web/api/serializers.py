from rest_framework import serializers
from web.models import Purchases, Comments, Projects, Plans, ToDo, Photos
from web.models import User, Employees, Geographical, Clients, Tasks, Likes
from rest_framework.authtoken.models import Token

#Serializer of Token model
class Token_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Token
        fileds = ("key",)

#Private serializer of User model
class User_Serializers_Private(serializers.ModelSerializer):
    #token = Token_Serializers(required=True)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
        #TODO: Add token field also ...

class User_Serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")

#Public serializer of User model
class User_Serializers_Public(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

#Serializer of Employees
class Employees_Serializers(serializers.ModelSerializer):
    user = User_Serializers_Public(required=False)

    class Meta:
        model = Employees
        fields = ("user", "post", "profile_pic")
    
    def create(self, validated_data):
        user = validated_data.pop("user")
        employer = Employees.objects.create(user=user, **validated_data)

        return employer


#Serializer of Clients
class Clients_Serializers(serializers.ModelSerializer):
    user = User_Serializers_Public(required=False)

    class Meta:
        model = Clients
        fields = "__all__"

#Serializer of Geographical
class Geographical_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Geographical
        fields = ("location", "latitude", "longitude")

#Serializer of Purchases model
class Projects_Serializers(serializers.ModelSerializer):
    employer = Employees_Serializers(required=False)
    client = Clients_Serializers(required=False)
    geographical = Geographical_Serializer(required=False)

    class Meta:
        model = Projects
        fields = ("id", "name", "start_date", "price", "done", "employer", "geographical", "client")
    
    def create(self, validated_data):
        user_email = validated_data.pop("employer")["user"]["email"]
        client_email = validated_data.pop("client")["user"]["email"]
        geographical_data = validated_data.pop("geographical")
        emp_user = User.objects.get(email=user_email)
        employer = Employees.objects.get(user=emp_user)
        client_user = User.objects.get(email=client_email)
        client = Clients.objects.get(user=client_user)
        geographical = Geographical.objects.create(**geographical_data)
        project = Projects.objects.create(employer=employer, client=client, geographical=geographical,
         **validated_data)
        return project
    
    def update(self, instance, validated_data):
        try:
            empolyer_data = validated_data.pop("employer")
            client_data = validated_data.pop("client")
            geographical_data = validated_data.pop("geographical")

            empolyer = instance.employer
            client = instance.client
            geographical = instance.geographical
        except:
            pass
#        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.price = validated_data.get('price', instance.price)
        instance.done = validated_data.get('done', instance.done)
        instance.save()

        return instance

class Tasks_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"
    
    def create(self, validated_data):
        project = validated_data.pop("project")
#        project_id = validated_data.pop("project")
#        project = Projects.objects.get(id=project_id)
        task = Tasks.objects.create(project=project, **validated_data)
        return task
    
    def update(self, instance, validated_data):
        project_id = validated_data.pop("project")

        project = instance.project

        instance.id = validated_data.get('id', instance.id)
        instance.subject = validated_data.get('subject', instance.id)
        instance.save()

        return instance

class ToDo_serializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"

    def create(self, validated_data):
#        task_id = validated_data.pop("task")
        task = validated_data.pop("task")
#        task = Tasks.objects.get(id=task_id)
        todo = ToDo.objects.create(task=task, **validated_data)

        return todo
    def update(self, instance, validated_data):
        task_id = validated_data.pop("task")

        task = instance.task

        instance.id = validated_data.get('id', instance.id)
        instance.id = validated_data.get('details', instance.id)
        instance.id = validated_data.get('done', instance.id)
        instance.save()

        return instance

class Plans_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = ("id", "photo", "data", "kind", "project")

    def create(self, validated_data):
        project_id = validated_data.pop("project")
        project = Projects.objects.get(id=project_id)
        plan = Plans.objects.create(project=project, **validated_data)
        return plan
    
    def update(self, instance, validated_data):
        project_id = validated_data.pop("project")

        project = instance.project

        instance.id = validated_data.get('id', instance.id)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.date = validated_data.get('date', instance.date)
        instance.kind = validated_data.get('kind', instance.kind)
        instance.save()

        return instance


#Serializer of Purchases model
class Purchases_serializers(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = ("buyer", "amount", "for_what", "date")

#Serializer of Comments model
class Comments_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

#Serializers of Photos
class Photos_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = "__all__"

class Likes_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"