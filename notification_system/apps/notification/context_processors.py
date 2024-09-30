from django.core.cache import cache
from .models import Notification


def unread_notification_count(request):
    if request.user.is_authenticated:
        cache_key = f"unread_notifications_{request.user.id}"
        unread_count = cache.get(cache_key)
        print(f"----------->>> from cache..... {unread_count}")
        if unread_count is None:
            print("------------> Get from database....................")
            unread_count = Notification.objects.filter(user=request.user, is_read=False).count()
            cache.set(cache_key, unread_count, 10)  # 10 second for cache
        return {'unread_notification_count': unread_count}
    return {'unread_notification_count': 0}