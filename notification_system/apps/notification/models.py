from django.db import models

from apps.account.models import Account


class Notification(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
