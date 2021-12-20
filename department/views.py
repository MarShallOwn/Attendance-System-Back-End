from Common_Responses import Bad_Response, Created_Response, No_Content_Response, Ok_Response
from department.serializers import departmentserializer
from .models import department
from rest_framework.decorators import api_view

#GET-Post
@api_view(['Get','Post'])
def Department_List(request):
    if request.method == 'GET':
        try:
            departments = department.objects.all()
        except:
            return Bad_Response(data=None,From='Get department')
        serializer = departmentserializer(departments, many=True)
        return Ok_Response(serializer.data)

    elif request.method == 'POST':
        serializer = departmentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Created_Response(serializer.data)
        else:
            return Bad_Response(data=serializer.errors,From=None)
    else:
            return Bad_Response('All departments')

@api_view(['GET','PUT','DELETE'])
def Department_pk(request, pk):
    try:
         departments = department.objects.get(pk=pk)
    except department.DoesNotExist:
        return Bad_Response(data= None,From='GET department pk')
         
    if request.method == 'GET':
        serializer = departmentserializer(departments)
        return Ok_Response(serializer.data)

    elif request.method == 'PUT':
        serializer = departmentserializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return No_Content_Response()
        else:
            return Bad_Response(data=serializer.errors,From=None)
    elif request.method == 'DELETE':
            department.delete()
            return No_Content_Response()
    else:
        return Bad_Response('All departments pk')
    
            