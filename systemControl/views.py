from Common_Responses import Bad_Response, Created_Response, No_Content_Response, Ok_Response
from .serializers import ControlSerializer
from .models import Control
from rest_framework.decorators import api_view


#GET-Post
@api_view(['GET'])
def SystemControl_List(request):
    if request.method == 'GET':
        try:
            control = Control.objects.all().first()
        except:
            return Bad_Response(data=None,From='DoesNotExist')
        serializer = ControlSerializer(control)
        return Ok_Response(serializer.data)
    else:
            return Bad_Response('All Control')


@api_view(['PUT'])
def SystemControl_pk(request):
    try:
         control = Control.objects.first()
    except Control.DoesNotExist:
        return Bad_Response(data= None,From='DoesNotExist')
    if request.method == 'PUT':
        serializer = ControlSerializer(control, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except:
                return No_Content_Response()
            return No_Content_Response()
        else:
            return Bad_Response(data=serializer.errors,From=None)
    else:
        return Bad_Response('SystemControl pk')
        
