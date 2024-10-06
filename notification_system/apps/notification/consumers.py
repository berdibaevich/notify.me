import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from django.apps import apps


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope['user'].is_authenticated:
            await self.accept()
            await self.channel_layer.group_add(f"notification_{self.scope['user'].id}", self.channel_name)

            await self.send_unread_notifications_count()
        else:
            await self.close()
            return

    async def disconnect(self, code):
        if self.scope['user'].is_authenticated:
            await self.channel_layer.group_discard(f"notification_{self.scope['user'].id}", self.channel_name)


    async def send_unread_notifications_count(self):
        unread_count = await self.get_unread_count(self.scope['user'])
        await self.send(
            text_data=json.dumps({'count': unread_count})
        )


    async def send_news_notification(self, event):
        user = self.scope['user']
        unread_count = await self.get_unread_count(user)
        await self.send(
            text_data=json.dumps({'count': unread_count})
        )


    async def send_notification_from_views(self, event):
        unread_count = await self.get_unread_count(event['who'])
        await self.send(
            text_data = json.dumps({'count': unread_count})
        )

    @database_sync_to_async
    def get_unread_count(self, user):
        from apps.notification.models import Notification
        return Notification.objects.filter(recipient = user, is_read = False).count()
