from django.contrib import admin
from .models import Account, UploadToAvatar

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_active', 'is_staff', 'is_superuser')


admin.site.register(UploadToAvatar)