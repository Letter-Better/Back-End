from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from user.models import User
from jwt import decode as jwt_decode
from jwt.exceptions import DecodeError, ExpiredSignatureError
from channels.middleware import BaseMiddleware
from main.settings import conf

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
        token: list = [item[1].decode() for item in scope["headers"] if item[0].decode()=='authentication']

        try:
            detail = jwt_decode(token[0][7:], conf["settings"]["SECRET_KEY"], conf["jwt"]["ALGORITHM"])
            scope["user"] = await get_user(detail["user_id"])
        except DecodeError:
            scope["user"] = AnonymousUser()
        except ExpiredSignatureError:
            scope["user"] = AnonymousUser()
        except IndexError:
            scope["user"] = AnonymousUser()
        return await super().__call__(scope, receive, send)
