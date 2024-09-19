from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Account
from .utils import get_upload_avatar_for_user


@receiver(post_save, sender = Account)
def add_photo(sender, instance, created, **kwargs):
    if created and instance.is_active: # when new account created so add photo
        print("Signals ADD PHOTO")
        instance.photo = get_upload_avatar_for_user()
        instance.save()
        