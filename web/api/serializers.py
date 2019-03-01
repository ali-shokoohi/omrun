from rest_framework import serializers
from ..models import Purchases, Comments

class Purchases_serializers(serializers.ModelSerializer):
    class Meta:
        model = Purchases

class Comments_serializers(serializers.ModelSerializer):
    class Meta:
        model = Comments