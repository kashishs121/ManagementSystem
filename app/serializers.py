from rest_framework import serializers
from .models import Users
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from .models import *
from .managers import UserManager

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username','password','role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        auth_user = Users.objects.create_user(**validated_data)
        # user.save()
        return auth_user


    # def create(self, validated_data):
    #     username = validated_data['username']

    #     # Check if a user with the given username already exists
    #     user_validation = Users.objects.filter(username=username).first()
    #     if user_validation:
    #         raise serializers.ValidationError({'username': 'User with this username already exists.'})

    #     auth_user = UserManager().create_user(**validated_data)
    #     return auth_user

# serializers.py


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookHotel
        fields = '__all__'


from rest_framework import serializers
from .models import BookSpecificHotel

class SpecificBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSpecificHotel
        fields = '__all__'