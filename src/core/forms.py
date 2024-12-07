from django import forms

from .models import Sugerencias_Comidas, Reservaciones, Pedidos



class Suerencias_ComidasForm(forms.ModelForm):
    class Meta:
        model = Sugerencias_Comidas
        fields = "__all__"


class ReservacionesForm(forms.ModelForm):
    class Meta:
        model = Reservaciones
        fields = "__all__"
        widget = {"reservacion_fecha": forms.DateInput(attrs={"type": "date"})}

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = "__all__"