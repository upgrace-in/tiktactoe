import asyncio
import json
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer
from tiktactoe_app.models import game, tiktactoe


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        
        game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_id = game_id
        self.game_room = game_id
        await self.channel_layer.group_add(
            self.game_room,
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        loaded_dict = json.loads(event.get('text', None))
        try:
            if loaded_dict['spectator'] is not None:
                response = {
                    'spectator': loaded_dict['spectator'],
                }
                await self.channel_layer.group_send(
                    self.game_room,
                    {
                        "type": "game_move",
                        "text": json.dumps(response)
                    }
                )    
        except KeyError:
            m = await self.save_move(self.game_id, loaded_dict['user'], loaded_dict['sm_nos'])
            response = {
                'user': m.user,
                'sm_nos': m.sm_nos,
                'symbol': m.symbol
            }
            await self.channel_layer.group_send(
                self.game_room,
                {
                    "type": "game_move",
                    "text": json.dumps(response)
                }
            )

    async def game_move(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect(self, event):
        print("disconnected", event)

    @database_sync_to_async
    def save_move(self, game_id, user, sm_nos):
        m = tiktactoe.objects.get(linker=game_id)
        symbol = '' 
        if m.first_player == user:
            symbol = 'cross'
        else:
            symbol = 'circle'
        return game.objects.create(link=m, user=user, sm_nos=sm_nos, symbol=symbol)