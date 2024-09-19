from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from apps.account.models import Account
from apps.blog.models import News
from .models import Notification



@receiver(post_save, sender = News)
def send_news_notification(sender, instance, created, **kwargs):
    if created:
        message = f"Taza xabar: {instance.title}"

        for account in Account.objects.all():
            Notification.objects.create(user = account, message = message)
            
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"notification_{account.id}",
                {
                    "type": "send_news_notification"
                }
            )
