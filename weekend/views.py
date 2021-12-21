from Common_Responses import Bad_Response, No_Content_Response, Created_Response, Ok_Response
from weekend.serializers import weekendserializer
from .models import weekend
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def weekend_List(request):
    if request.method == 'GET':
        try:
            weekends = weekend.objects.all().first()
        except:
            return Bad_Response(data=None,From='GET weekend')
        serializer = weekendserializer(weekends)
        return Ok_Response(serializer.data)

    elif request.method == 'POST':
        serializer = weekendserializer(data=request.data)
        if serializer.is_valid():
            if int(weekend.objects.count())!=1:
                serializer.save()
                return Created_Response()
            else:
                return Bad_Response(data="weekend must contain one object")
        else:
                return Bad_Response(data=serializer.errors)
    else:
            return Bad_Response('All weekend')

@api_view(['GET','PUT'])
def weekend_pk(request, pk):
    try:
        weekends = weekend.objects.get(pk=pk)
    except weekend.DoesNotExist:
        return Bad_Response(data= None,From='GET weekend pk')
         
    if request.method == 'GET':
        serializer = weekendserializer(weekends)
        return Ok_Response(serializer.data)

    elif request.method == 'PUT':
        serializer = weekendserializer(weekends, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return No_Content_Response()
        else:
            return Bad_Response(data=serializer.errors,From=None)
    else:
        return Bad_Response('All weekends pk')