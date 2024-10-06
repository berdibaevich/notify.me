from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count, Exists, OuterRef
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from apps.notification.models import Notification

from . import forms
from .models import Account
from ..blog.models import Follow


def sign_in(request):
    if request.method == 'POST':
        form = forms.SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data['user_name'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect("blog:home")
    else:
        form = forms.SignInForm()
    
    context = {
        "form": form
    }
    return render(request, 'account/sign_in.html', context)



def sign_out(request):
    logout(request)
    return redirect('blog:home')


@login_required
def authors(request):
    is_following_subquery = Follow.objects.filter(
        follower = request.user, following = OuterRef("pk")
    )
    authors = Account.objects.annotate(
        nums_of_follower = Count("following", distinct=True),
        nums_of_following = Count("follower", distinct=True),
        is_following = Exists(is_following_subquery)
    ).exclude(id = request.user.id)
    return render(request, 'account/authors.html', {'authors': authors})


def followOrUnfollow(request):
    if request.method == 'POST':
        user = request.user
        current_action = request.POST.get("current_action")
        to_user = int(request.POST.get("to_user"))
        current_user = int(request.POST.get("current_user"))

        to_user_obj = Account.objects.get(id = to_user)
        if current_action == "follow" and user.id == current_user:
            Follow.objects.create(follower = user, following = to_user_obj)

            # Send notification
            Notification.objects.create(recipient = to_user_obj, notification_type = 1, object_id = current_user)
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"notification_{to_user_obj.id}",
                {
                    "type": "send_notification_from_views",
                    "who": to_user_obj
                }
            )
            return JsonResponse({'success': 200})
        elif current_action == "unfollow" and user.id == current_user:
            obj = Follow.objects.get(follower = user, following = to_user_obj)
            obj.delete()
            return JsonResponse({'success': 200})
