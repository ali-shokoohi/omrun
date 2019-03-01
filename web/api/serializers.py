from rest_framework import serializers
from ..models import Purchases, Comments

class Purchases_serializers(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = ("buyer", "amount", "for_what", "date")

class Comments_serializers(serializers.ModelSerializer):
    class Meta:
        model = Comments