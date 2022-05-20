from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Profile, Skill, SkillSet, UserSkill


class AddSkillForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['skill_set']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputUsername",
                "placeholder": "Имя пользователя",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mt-2",
                "id": "inputPassword",
                "placeholder": "Почта",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mt-2",
                "id": "inputPassword",
                "placeholder": "Пароль",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mt-2",
                "id": "inputPassword",
                "placeholder": "Повторите пароль",
            }
        ),
    )


class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputUsername",
                "placeholder": "Имя пользователя",
            }
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mt-2",
                "id": "inputUsername",
                "placeholder": "Пароль",
            }
        ),
    )
