from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from . import forms


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
