from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("betty's/confirmacion/", views.confirmacion, name="confirmacion"),
    path("betty's/pedido/", views.pedido_create, name="pedido"),
    path("betty's/reservacion/", views.reservacion_create, name="reservacion"),
    path("betty's/sugerencia/", views.sugerencia_create, name="sugerencia"),
    path("bettr's/menu/", views.menu, name="menu")
]