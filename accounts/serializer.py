# myapp/serializers.py
from rest_framework import serializers
from .models import UserProfile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'full_name', 'email', 'user_type', 'password']
        extra_kwargs = {'password': {'write_only': True}}
 