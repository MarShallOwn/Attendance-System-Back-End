from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
import jwt
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import LoginSerializer, LogoutSerializer, UpdateSerializer, UserSerializers
# I Combine all Repeated Response and status code in one file ('Don't Repeat Your Self')
from Common_Responses import *
#the class resposible for sending emails
from .Util import Util
#this is used to get the current site that we run now
from django.contrib.sites.shortcuts import get_current_site
#used to reverse the name of url to redirect use to 
#another endpoint
from django.urls import reverse

from authentication import serializers

#Create and List The Users =>allow GET and POST
@api_view(['GET','POST'])
def Registration(request):
    if request.method=='GET':
        try:
            users = User.objects.all()
        except:
             return Bad_Response(data=None,From='GET Registration User')
        serializers = UserSerializers(instance=users,many=True)
        return Ok_Response(serializers.data)
    
    elif request.method=='POST':
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid():
            instance =serializers.save()
            instance.set_password(instance.password)
            instance.save()
            return Created_Response()
        else:
            return Bad_Response(data=serializers.errors,From=None)
    else:
        return Bad_Response(data=None,From='ALL Regestration User')

#Edit,GET specific user, Delete
@api_view(['GET','PUT','DELETE'])
def Mentainanace(request,pk):
    try:
        user = User.objects.get(id=pk)
    except:
        return Bad_Response(data=None,From='Try Mentainance of User')
    if request.method == 'PUT':
        deserializer = UpdateSerializer(instance=user,data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return No_Content_Response()
        else:
            return Bad_Response(data=deserializer.errors,From='PUT Mentainance User')
    elif request.method == 'GET':
        serializers = UserSerializers(instance=user)
        return Ok_Response(data=serializers.data)
    elif request.method == 'DELETE':
        user.delete()
        return No_Content_Response()
    else:
        return Bad_Response(data=None,From='ALL Mentainance User')

@swagger_auto_schema(method='POST',request_body=LoginSerializer)
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def Login(request):
        serializers = LoginSerializer(data=request.data)
        if serializers.is_valid():
            return Ok_Response(serializers.data)
        else:
            return Unautherized_Response(serializers.errors)
swagger_auto_schema(method='POST',request_body=LogoutSerializer)
@api_view(['POST'])
def Logout(request):
    serializers = LogoutSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return No_Content_Response()
    else:
        return Unautherized_Response(serializers.errors)

@api_view(['GET'])
def AuthenticatedUser(request):
    serializers= UserSerializers(request.user)
    return Ok_Response(serializers.data)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def ResetPassword(request):
    #send an email with password
    try:
        user = User.objects.get(email = request.data['email'])
    except:
        return Bad_Response(data=None,From="Reseting This User with this email")
    token = user.tokens()['access']
    Code = str(token)
    data = {
        'subject':'Reset Your Password',
        'body':'HI <b>' + user.username+'</b>,\n<strong>Copy the code below\nCode</strong>\n'+'<h3 style="color:red">'+Code+'</h3>',
        'to': user.email,
        }
    Util.send_email(data)
    return Ok_Response(data="Reseting Email Has Been Sent.")

@api_view(['PUT'])
@authentication_classes([])
@permission_classes([])
def UpdatePassword(request):
    token = request.data['code']
    try:
        pyload = jwt.decode(token,settings.SECRET_KEY,algorithms='HS256')
        user = User.objects.get(email=pyload['email'])
        if user:
            if len(request.data['password'])>=6:
                user.set_password(request.data['password'])
                user.save()
                return No_Content_Response()
            return Bad_Response(From="Password should be 6 char at least")
        return Bad_Response(From="You Are Not User")
    except jwt.ExpiredSignatureError as ex:
        return Unautherized_Response("Reseting Link Expired")
    
    except jwt.exceptions.DecodeError as ex:
        return Bad_Response(From="Invalid Decoding")
    except:
        return Bad_Response(From="updating Password")
    
    