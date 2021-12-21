from rest_framework.authentication import get_authorization_header,BaseAuthentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from authentication.models import User
class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):

        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(" ")

        if len(auth_token) !=2:
            raise exceptions.AuthenticationFailed('Token not Valid')

        token = auth_token[1]
        try:
            pyloads = jwt.decode(token,settings.SECRET_KEY,algorithms='HS256')
            user_id = pyloads['user_id']
            user = User.objects.get(id = user_id)
            return (user,token)
        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed("Token is expired, Login again")
        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed("Token is invalid")
        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed("You Are Not System user") 
