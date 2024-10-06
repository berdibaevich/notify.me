from django.shortcuts import render
from .models import Notification


def notification_list(request):
    context = {}
    if request.user.is_authenticated:
        notify_list = Notification.objects.filter(recipient = request.user, is_read = False)
        context['notifications'] = notify_list
    return render(request, "notification/notification.html", context)



