from django.utils.translation import deactivate_all
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
    elif str.lower(name) == 'unauth':
        return status.HTTP_401_UNAUTHORIZED
    else:
        raise ValueError


def Bad_Response(data=None,From=None):
    if data!=None:
        return Response({
                'error':data,
                'data':None},
                status=Status_Code('bad'))
    else:
        return Response({
                'error':f'Bad Request in {From}',
                'data':None,},
                status=Status_Code('bad'))
        
def Ok_Response(data):
    return Response({
                'error':None,
                'data':data},
                status=Status_Code('ok'))

def No_Content_Response():
    return Response({
                'error':None,
                'data':None,},
                status=Status_Code('nocontent'))

def Created_Response():
    return Response({
                'error':None,
                'data':None,},
                status=Status_Code('created'))

def Unautherized_Response(data = "Unautherized Request"):
    return Response({
                'error':data,
                'data':None},
                status=Status_Code('unauth'))
