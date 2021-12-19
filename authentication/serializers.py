from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=6,write_only=True)
    class Meta:
        model = User
        fields = ['id','nationalID','username','firstname','lastname','email','phoneNumber','password']
        read_only_field = ['id']
        def create(self,validated_data):
            return User.objects.create_user(**validated_data) 
        
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=6,write_only=True)
    email = serializers.EmailField(max_length = 150,min_length=11)
    class Meta:
        model = User
        fields = ['id','email','username','firstname','lastname','password','tokens']
        read_only_fields = ['id','username','firstname','lastname','tokens']
    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        user = auth.authenticate(email = email,password = password)
        if not user:
            raise AuthenticationFailed("Invalid Credentials")
        return {
            'id':user.id,
            'email':user.email,
            'username':user.username,
            'firstname':user.firstname,
            'lastname':user.lastname,
            'tokens':user.tokens,
        }