from rest_framework import serializers
from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializers
# I Combine all Repeated Response and status code in one file ('Don't Repeat Your Self')
from Common_Responses import *

#Create and List The Users =>allow GET and POST
@api_view(['GET','POST'])
def Registration(request):
    if request.method=='GET':
        try:
            users = User.objects.all()
        except:
            return Bad_Response('GET Registration User')
        serializers = UserSerializers(instance=users,many=True)
        return Ok_Response(serializers.data)
    
    elif request.method=='POST':
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Created_Response(serializers.data)
        else:
            return Bad_Response('POST Regestration User')
    else:
        return Bad_Response('ALL Regestration User')

#Edit,GET specific user, Delete
@api_view(['GET','PUT','DELETE'])
def Mentainanace(request,pk):
    try:
        user = User.objects.get(id=pk)
    except:
        return Bad_Response('Try Mentainance of User')
    if request.method == 'PUT':
        deserializer = UserSerializers(instance=user,data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Ok_Response(deserializer.data)
        else:
            return Bad_Response('PUT Mentainance User')
    else:
        return Bad_Response('ALL Mentainance User')






