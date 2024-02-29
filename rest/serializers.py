from rest_framework import serializers
from registration.models import Regular_User
from main.models import Shop


class RegularUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regular_User
        fields = ['id', 'username', 'password', 'email']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'price', 'name', 'img_url', 'description', 'rating', 'create_date']