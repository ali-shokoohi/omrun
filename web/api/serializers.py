from rest_framework import serializers
from web.models import Purchases, Comments, Projects, Plans, User, Employees, Geographical, Clients
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

#Public serializer of User model
class User_Serializers_Public(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

#Serializer of Employees
class Employees_Serializers(serializers.ModelSerializer):
    user = User_Serializers_Public(required=True)

    class Meta:
        model = Employees
        fields = ("user", "post", "profile_pic")

#Serializer of Clients
class Clients_Serializers(serializers.ModelSerializer):
    user = User_Serializers_Public(required=True)

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
    employer = Employees_Serializers(required=True)
    client = Clients_Serializers(required=True)
    geographical = Geographical_Serializer(required=True)

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
        empolyer_data = validated_data.pop("employer")
        client_data = validated_data.pop("client")
        geographical_data = validated_data.pop("geographical")

        empolyer = instance.employer
        client = instance.client
        geographical = instance.geographical

        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.price = validated_data.get('price', instance.price)
        instance.done = validated_data.get('done', instance.done)
        instance.save()

        return instance


class PLans_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = ("photo", "data", "kind")

#Serializer of Purchases model
class Purchases_serializers(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = ("buyer", "amount", "for_what", "date")

#Serializer of Purchases model
class Comments_serializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("author", "text", "date")