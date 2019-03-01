from rest_framework import serializers
from ..models import Purchases, Comments

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