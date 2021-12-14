from rest_framework import status
from rest_framework.response import Response

def Status_Code(name):
    if str.lower(name) == 'bad':
        return status.HTTP_400_BAD_REQUEST

    elif str.lower(name) == 'ok':
        return status.HTTP_200_OK
    
    elif str.lower(name) == 'nocontent':
        return status.HTTP_204_NO_CONTENT
    
    elif str.lower(name) == 'created':
        return status.HTTP_201_CREATED
    else:
        raise ValueError


def Bad_Response(From):
    return Response({
                'error':f'BAD REQUEST in {From}',
                'data':None},
                status=Status_Code('bad'))

def Ok_Response(data):
    return Response({
                'error':None,
                'data':data},
                status=Status_Code('ok'))

def No_Content_Response():
    return Response({
                'error':None,
                'data':None},
                status=Status_Code('nocontent'))

def Created_Response(data):
    return Response({
                'error':None,
                'data':data},
                status=Status_Code('created'))
