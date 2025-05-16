from django import forms

from .models import Menu

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


def validatefood_name(name: str):
    if name:
        if not name.__contains__(','):
            raise forms.ValidationError('Si Solo Hay una Comida Pon una Coma al Final')
        if name.endswith(','):
            return name.replace(',', '')
    return name


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['food_name', 'price', 'image']
        labels = {
            'food_name': 'Comidas (Separadas por Comas)',
            'price': 'Precio (Solo Para el Especial)',
            'image': 'Imagen en el Menu'
        }

    def clean_food_name(self):
        name: str = self.cleaned_data.get('food_name', '')
        return validatefood_name(name)


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