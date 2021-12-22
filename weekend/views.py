from Common_Responses import Bad_Response, No_Content_Response, Created_Response, Ok_Response
from weekend.serializers import weekendserializer
from .models import weekend
from rest_framework.decorators import api_view

@api_view(['GET'])
def weekend_List(request):
    if request.method == 'GET':
        try:
            weekends = weekend.objects.all().first()
        except:
            return Bad_Response(data=None,From='GET weekend')
        serializer = weekendserializer(weekends)
        return Ok_Response(serializer.data)
    else:
        return Bad_Response('All weekend')

@api_view(['PUT'])
def weekend_pk(request):
    try:
        weekends = weekend.objects.all().first()
    except weekend.DoesNotExist:
        return Bad_Response(data= None,From='GET weekend pk')
    if request.method == 'PUT':
        serializer = weekendserializer(weekends, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return No_Content_Response()
        else:
            return Bad_Response(data=serializer.errors,From=None)
    else:
        return Bad_Response('All weekends pk')