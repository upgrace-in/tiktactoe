import asyncio
import json
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer
from . import models


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        
        game_id = self.scope['url_route']['kwargs']['game_id']
        print(game_id)
        self.game_room = game_id
        await self.channel_layer.group_add(
            self.game_room,
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        print("received", event)
        main_dict = event.get('text', None)
        if main_dict is not None:
            loaded_dict = json.loads(main_dict)
            myresponse = {
                'sm_nos': loaded_dict["sm_nos"]
            }
            new_event = {
                "type": "websocket.send",
                "text": json.dumps(myresponse)
            }
            await self.channel_layer.group_send({
                self.game_room,
                {
                    "type": "game_move",
                    "message": "hello"
                }
            })

    async def game_move(self, event):
        print('message', event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)

    @database_sync_to_async
    def get_move(self, game_id, user, sm_nos):
        m = models.tiktactoe.objects.get(linker=game_id)
        symbol = '' 
        if m.first_player == user:
            symbol = 'cross'
        else:
            symbol = 'circle'
        lnk = models.game.objects.create(link=m, user=user, sm_nos=sm_nos, symbol=symbol)
        lnk.save()
        return lnk