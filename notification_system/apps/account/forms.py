from django import forms
from .models import Account


class SignInForm(forms.Form):
    user_name = forms.CharField(
        max_length=50,
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3'
        })
    )

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        if not Account.objects.filter(username=user_name).exists():
            raise forms.ValidationError("Username naduris kiritdin'iz.")
        return user_name
