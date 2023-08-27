from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.ModelSerializer):
    model = Menu
    fields = ['id', 'title', 'price', 'inventory']