#learn to write middlewares in python
from channels.db import database_sync_to_async
from urllib.parse import parse_qs
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser

from channels.layers import get_channel_layer

@database_sync_to_async
def get_user(scope):
    try:
        token_key = parse_qs(scope['query_string'].decode('utf-8'))['token'][0]
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()
    except KeyError:
        return AnonymousUser()

class TokenAuthMiddleWare:
    def __init__(self,inner):
        self.inner = inner
        print("initialize")    
    def __call__(self,scope):
        return TokenAuthMiddleWareInstance(scope,self)

class TokenAuthMiddleWareInstance:
    def __init__(self,scope,middleware):
        self.scope = dict(scope)
        self.inner = middleware.inner

    async def __call__(self,receive,send):
        self.scope['user'] = await get_user(self.scope)
        inner = self.inner(self.scope)#calling next consumer/middleware.
        return await inner(receive,send)
        
