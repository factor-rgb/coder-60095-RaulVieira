from django import forms

from .models import Pedidos, Reservaciones, Sugerencias_Comidas, Menu


class Suerencias_ComidasForm(forms.ModelForm):
    class Meta:
        model = Sugerencias_Comidas
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