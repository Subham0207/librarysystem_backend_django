from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

from django.contrib.auth.models import AnonymousUser

class async_demoConsumer(AsyncJsonWebsocketConsumer): 
    async def connect(self,*args, **kwargs):
        self.group_name = 'demo_consumer'
        await (self.channel_layer.group_add)(
            self.group_name,self.channel_name
        )
        await self.accept()
        #received scope from middle ware
        if self.scope['user'] == AnonymousUser():
            await self.send(text_data=json.dumps({'Authentication_status':'False'}))
            await self.close()
        else:
            await self.send(text_data=json.dumps({'Authentication_Status':'True'}))
        
    async def disconnect(self, code):
        return await super().disconnect(code)