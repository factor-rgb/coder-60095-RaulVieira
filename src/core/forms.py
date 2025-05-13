from django import forms


from .models import Menu


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['food_name', 'price', 'image']
        labels = {
            'food_name': 'Comidas (Separadas por Comas)',
            'price': 'Precio (Solo Para el Especial)',
            'image': 'Imagen en el Menu'
        }


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']