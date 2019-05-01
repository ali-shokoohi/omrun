from rest_framework import serializers
from web.models import Purchases, Comments, Projects, Plans, User, Employees
from rest_framework.authtoken.models import Token

#Serializer of Token model
class Token_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Token
        fileds = ("key",)

#Serializer of User model
class User_Serializers(serializers.ModelSerializer):
    #token = Token_Serializers(required=True)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
        #TODO: Add token field also ...


#Serializer of Employees
class Employees_Serializers(serializers.ModelSerializer):
    user = User_Serializers(required=True)

    class Meta:
        model = Employees
        fields = ("user", "post", "profile_pic")
#Serializer of Purchases model
class Projects_Serializers(serializers.ModelSerializer):
    employer = Employees_Serializers(required=True)

    class Meta:
        model = Projects
        fields = ("id", "name", "employer")

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