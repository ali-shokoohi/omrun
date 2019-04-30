from rest_framework import serializers
from web.models import Purchases, Comments, Projects

#Serializer of Purchases model
class Projects_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("id", "name", "employer")

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