from django import forms


from .models import Pedidos, Reservaciones, SugerenciasComidas, Menu


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class Suerencias_ComidasForm(forms.ModelForm):
    class Meta:
        model = SugerenciasComidas
        fields = "__all__"


class ReservacionesForm(forms.ModelForm):
    class Meta:
        model = Reservaciones
        fields = "__all__"
        widgets = {'reservacion_fecha': forms.DateInput(attrs={"type": "date"})}


class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = "__all__"


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"


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