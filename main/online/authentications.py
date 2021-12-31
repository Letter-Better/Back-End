from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from user.models import User
from jwt import decode as jwt_decode
from channels.middleware import BaseMiddleware

@database_sync_to_async
def get_user(id):
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        return AnonymousUser()

class JWTAuthenticationMiddleware(BaseMiddleware):

    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        print(scope["headers"])
        try:
            token = ...
            id = jwt_decode()
        except:
            ...
        #return await super().__call__(scope, receive, send)