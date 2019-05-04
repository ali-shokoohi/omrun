from rest_framework import serializers
from web.models import Purchases, Comments, Projects, Plans, User, Employees, Geographical
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

#Serializer of Geographical
class Geographical_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Geographical
        fields = ("location", "latitude", "longitude")

#Serializer of Purchases model
class Projects_Serializers(serializers.ModelSerializer):
    employer = Employees_Serializers(required=True)
    geographical = Geographical_Serializer(required=True)

    class Meta:
        model = Projects
        fields = ("id", "name", "start_date", "price", "done", "employer", "geographical")

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