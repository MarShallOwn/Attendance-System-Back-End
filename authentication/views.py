from rest_framework import serializers
from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import status

#Create and List The Users =>allow GET and POST
@api_view(['GET','POST'])
def Registration(request):
    if request.method=='GET':
        try:
            users = User.objects.all()
        except:
            return Response({
                'error':'BAD REQUEST in GET Registration User',
                'data':None},
                status=status.HTTP_400_BAD_REQUEST)
        serializers = UserSerializers(instance=users,many=True)
        return Response({
                'error':None,
                'data':serializers.data},
                status=status.HTTP_200_OK)
    
    elif request.method=='POST':
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({
                'error':None,
                'data':serializers.data},
                status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error':'invalid Data in POST Regestration User',
                'data':None},
                status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({
                'error':'BAD REQUEST in All Registration User',
                'data':None},
                status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def Mentainanace(request,pk):
    try:
        user = User.objects.get(id=pk)
    except:
        return Response({
                'error':'BAD REQUEST in PUT Mentainance of User',
                'data':None},
                status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        deserializer = UserSerializers(instance=user,data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response({
                'error':None,
                'data':deserializer.data},
                status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                'error':deserializer.errors,
                'data':None},
                status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
                'error':'BAD REQUEST in ALL Mentainance User',
                'data':None},
                status=status.HTTP_400_BAD_REQUEST)






