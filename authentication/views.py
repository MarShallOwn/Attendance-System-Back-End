from datetime import datetime
from .models import User
from rest_framework.decorators import api_view, authentication_classes
from .serializers import LoginSerializer, UserSerializers
# I Combine all Repeated Response and status code in one file ('Don't Repeat Your Self')
from Common_Responses import *
#allow me to handle the authentiction of user (Login) by email,password 
from django.contrib.auth import authenticate
#the class resposible for sending emails
from .Util import Util
#this is used to get the current site that we run now
from django.contrib.sites.shortcuts import get_current_site
#used to reverse the name of url to redirect use to 
#another endpoint
from django.urls import reverse

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
        deserializer = UserSerializers(instance=user,data=request.data)
        if deserializer.is_valid():
            instance =deserializer.save()
            instance.set_password(instance.password)
            instance.save()
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


@api_view(['POST'])
@authentication_classes([])
def Login(request):
    email = request.data['email']
    password = request.data['password']
    user = authenticate(username=email,password=password)
    if user:
        serializers = LoginSerializer(user)
        user.last_login = datetime.utcnow()
        return Ok_Response(serializers.data)
    else:
        return Unautherized_Response('Invalid Credntiaol')


@api_view(['GET'])
def AuthenticatedUser(request):
    serializers= UserSerializers(request.user)
    return Ok_Response(serializers.data)


@api_view(['POST'])
@authentication_classes([])
def ResetPassword(request):
    #send an email with password
    try:
        user = User.objects.get(email = request.data['email'])
    except:
        return Bad_Response(data=None,From="Reseting This User with this email")
    token = user.token
    current_site = get_current_site(request).domain
    relative_link = reverse('employerlist')
    urlToUpdatePass = 'http://'+current_site+relative_link+"?Authorization=Bearer%20"+str(token)
    data = {
        'domain':urlToUpdatePass,
        'subject':'Reset Your Password',
        'body':'Hi ' + user.username+', Use link below to update your password \n'+urlToUpdatePass,
        'to': user.email,
        }
    Util.send_email(data)
    return Ok_Response(data="Reseting Email Has Been Sent.")

@api_view(['PUT'])
def UpdatePassword(request):
    try:
        serializedUser = UserSerializers(request.user)
        user = User.objects.get(email=serializedUser.data['email'])
    except:
        return Bad_Response(From="Updata user Password") 
    if user:
        if len(request.data['password'])>=6:
            user.set_password(request.data['password'])
            user.save()
            return No_Content_Response()
        return Bad_Response(From="Password should be 6 char at least")
    return Bad_Response(From="You Are Not User")
    