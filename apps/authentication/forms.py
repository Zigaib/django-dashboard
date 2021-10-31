# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from apps.authentication.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuário",
                "class": "form-control",
                "autocomplete": "nope",

            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control",
                "autocomplete": 'new-password'
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuario",
                "class": "form-control",
                'autocomplete': 'off'
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome",
                "class": "form-control"
            }
        ))

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sobrenome",
                "class": "form-control"
            }
        ))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirmar Senha",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name', 'password1', 'password2')


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sobrenome",
                "class": "form-control"
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    
        
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    sexo = forms.ChoiceField(
        choices=(
            ('M', 'Masculino'),
            ('F', 'Femenino'),
        ),
        widget=forms.Select(
            attrs={
                "placeholder": "Sexo",
                "class": "form-control"
            }
        ))
    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Data de nascimento",
                "class": "form-control"
            }
        ))
    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefone",
                "class": "form-control"
            }
        ))
    endereco = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Endereço",
                "class": "form-control"
            }
        ))
    cidade = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Cidade",
                "class": "form-control"
            }
        ))
    estado = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Estado",
                "class": "form-control"
            }
        ))
    sobre = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Sobre",
                "class": "form-control",
                "rows": '3'
            }
        ))
    
    cargo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Cargo",
                "class": "form-control input-border-bottom",
                "id": "inputFloatingLabel",
                "style": "text-align: -webkit-center;padding-bottom: 0; "
            }
        ))

    class Meta:
        model = Profile
        fields = ('data_nascimento', 'sexo', 'telefone', 'endereco', 'cidade', 'estado', 'sobre', 'cargo')