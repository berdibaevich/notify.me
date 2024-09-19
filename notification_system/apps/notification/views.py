from django.shortcuts import render
from .models import Notification


def notification_list(request):
    notify_list = Notification.objects.filter(user = request.user, is_read = False)
    return render(request, "notification/notification.html", {'notifications': notify_list})



