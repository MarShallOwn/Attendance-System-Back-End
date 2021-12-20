from Common_Responses import Bad_Response, Created_Response, No_Content_Response, Ok_Response
from systemControl import UpdateSystemControl
from .serializers import ControlSerializer
from .models import Control
from rest_framework.decorators import api_view


#GET-Post
@api_view(['GET','POST'])
def SystemControl_List(request):
    if request.method == 'GET':
        try:
            control = Control.objects.all()
        except:
            return Bad_Response(data=None,From='Get Control')
        serializer = ControlSerializer(control, many=True)
        return Ok_Response(serializer.data)

    elif request.method == 'POST':
        serializer = ControlSerializer(data=request.data)
        if serializer.is_valid():
            if int(Control.objects.count())!=1:
                serializer.save()
                return Created_Response()
            else:
                return Bad_Response(data="Control must contain one object")
        return Bad_Response(data=serializer.errors)
    else:
            return Bad_Response('All Control')


@api_view(['GET','PUT','DELETE'])
def SystemControl_pk(request, pk):
    try:
         control = Control.objects.get(pk=pk)
    except Control.DoesNotExist:
        return Bad_Response(data= None,From='GET control pk')
         
    if request.method == 'GET':
        serializer = ControlSerializer(control)
        return Ok_Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ControlSerializer(control, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except:
                return No_Content_Response()
            return No_Content_Response()
        else:
            return Bad_Response(data=serializer.errors,From=None)
    elif request.method == 'DELETE':
            control.delete()
            return No_Content_Response()
    else:
        return Bad_Response('All controls pk')
        
