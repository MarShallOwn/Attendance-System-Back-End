from Common_Responses import Bad_Response, Created_Response, No_Content_Response, Ok_Response
from holiday.serializers import holidayserializer
from .models import holiday
from rest_framework.decorators import api_view

#GET-Post
@api_view(['GET','POST'])
def holiday_List(request):
    if request.method == 'GET':
        try:
            holidays = holiday.objects.all()
        except:
            return Bad_Response(data=None,From='GET holiday')
        serializer = holidayserializer(holidays, many=True)
        return Ok_Response(serializer.data)

    elif request.method == 'POST':
        serializer = holidayserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Created_Response()
        else:
            return Bad_Response(data=serializer.errors,From=None)
    else:
            return Bad_Response('All holidays')

@api_view(['GET','PUT','DELETE'])
def holiday_pk(request, id):
    try:
        holidays = holiday.objects.get(id=id)
    except holiday.DoesNotExist:
        return Bad_Response(data= None,From='GET holiday pk')
         
    if request.method == 'GET':
        serializer = holidayserializer(holidays)
        return Ok_Response(serializer.data)

    elif request.method == 'PUT':
        serializer = holidayserializer(holidays, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return No_Content_Response()
        else:
            return Bad_Response(data=serializer.errors,From=None)
    elif request.method == 'DELETE':
            holidays.delete()
            return No_Content_Response()
    else:
        return Bad_Response('All holidays pk')