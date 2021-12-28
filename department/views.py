from Common_Responses import Bad_Response, Created_Response, No_Content_Response, Ok_Response
from department.serializers import departmentserializer
from .models import department
from rest_framework.decorators import api_view

def addDepartmentHeadNameToModel(serializer):
    if str(type(serializer.data))=="<class 'rest_framework.utils.serializer_helpers.ReturnList'>":
        for depts in serializer.data:
            dept= department.objects.get(id = depts['id'])
            if dept.departmentHeadID !=None:
                depts['departmentHeadName'] =dept.departmentHeadID.firstname + ' ' + dept.departmentHeadID.lastname
        return True
    else:
        dept = serializer.data
        dep= department.objects.get(id = dept['id'])
        if dep.departmentHeadID !=None:
            dept['departmentHeadName'] = dep.departmentHeadID.firstname + ' ' + dep.departmentHeadID.lastname
        return dept


#GET-Post
@api_view(['GET','POST'])
def Department_List(request):
    if request.method == 'GET':
        try:
            departments = department.objects.all()
        except:
            return Bad_Response(data=None,From='Get department')
        serializer = departmentserializer(departments, many=True)
        addDepartmentHeadNameToModel(serializer)
        return Ok_Response(serializer.data)

    elif request.method == 'POST':
        serializer = departmentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Created_Response()
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
        dept = addDepartmentHeadNameToModel(serializer)
        return Ok_Response(dept)

    elif request.method == 'PUT':
        serializer = departmentserializer(departments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return No_Content_Response()
        else:
            return Bad_Response(data=serializer.errors,From=None)
    elif request.method == 'DELETE':
            departments.delete()
            return No_Content_Response()
    else:
        return Bad_Response('All departments pk')
    
            