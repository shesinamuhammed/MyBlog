from django import forms
from django.contrib.auth.models import User

from .models import Blog


class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'body')
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if len(title)<5:
            self.add_error('title','Please enter longer number')
        return cleaned_data


class SignUpForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': 'The two password fields didn’t match.',
        'short_password' : 'Must be minimum 8 characters',
    }
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        if len(password1)<8:
            raise forms.ValidationError(
                self.error_messages['short_password'],
                code='short_password',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user

      



