from django.db.models import fields
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=6,write_only=True)
    
    class Meta:
        model = User
        fields = ['id','nationalID','username','firstname','lastname','email','phoneNumber','password']
        read_only_field = ['id']
        def create(self,validated_data):
            return User.objects.create_user(**validated_data)
        
