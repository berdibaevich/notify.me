from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('authors/', views.authors, name = "authors"),
    path('sign_in/', views.sign_in, name = "sign_in"),
    path('sign_out/', views.sign_out, name = "sign_out"),
    path('followOrUnfollow/', views.followOrUnfollow, name="followOrUnfollow")
]