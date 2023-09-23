import jwt
from rest_framework import authentication, exceptions

from sample import settings
from django.contrib.auth.models import User

class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request);

        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split(' ')

        try:
            print("token is ", token)
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            print("payload is", payload)
            user = User.objects.get(email=payload['email'])
            return (user, token)
        except jwt.DecodeError as identifier:
            print("error is",identifier)
            raise exceptions.AuthenticationFailed('Your token is invalid')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Your token is Expired')

        return super().authenticate(request)