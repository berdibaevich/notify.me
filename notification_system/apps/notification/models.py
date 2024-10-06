from django.db import models

from apps.account.models import Account


class Notification(models.Model):
    TYPE = (
        (1, 'FOLLOW'),
        (2, 'BLOG'),
        (3, 'NEWS'),
    )
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="notifications")
    notification_type = models.IntegerField(choices=TYPE)
    object_id = models.IntegerField() # Follow, Blog, News id
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.notification_type)
    