from Common_Responses import Bad_Response, Created_Response, No_Content_Response, Ok_Response
from role.serializers import roleserializer
from .models import role
from rest_framework.decorators import api_view

# Create your views here.
#GET-Post
@api_view(['GET','POST'])
def role_List(request):
    if request.method == 'GET':
        try:
            roles = role.objects.all()
        except:
            return Bad_Response(data=None,From='GET role')
        serializer = roleserializer(roles, many=True)
        return Ok_Response(serializer.data)

    elif request.method == 'POST':
        serializer = roleserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Created_Response()
        else:
            return Bad_Response(data=serializer.errors,From=None)
    else:
            return Bad_Response('All roles')

@api_view(['GET','PUT','DELETE'])
def role_pk(request, pk):
    try:
         roles = role.objects.get(pk=pk)
    except role.DoesNotExist:
        return Bad_Response(data= None,From='GET role pk')
         
    if request.method == 'GET':
        serializer = roleserializer(roles)
        return Ok_Response(serializer.data)

    elif request.method == 'PUT':
        serializer = roleserializer(roles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return No_Content_Response()
        else:
            return Bad_Response(data=serializer.errors,From=None)
    elif request.method == 'DELETE':
            if roles.roleName!='manager' or roles.roleName!='employer':
                roles.delete()
                return No_Content_Response()
            return Bad_Response(data={'managerRole':"Can't Be Deleted",'employerRole':"Can't Be Deleted"})
    else:
        return Bad_Response('All role pk')