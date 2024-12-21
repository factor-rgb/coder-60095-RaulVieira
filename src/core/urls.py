from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("betty's/confirmacion/", views.confirmacion, name="confirmacion"),
    path("betty's/pedido/", views.pedido_create, name="pedido"),
    path("betty's/reservacion/", views.reservacion_create, name="reservacion"),
    path("betty's/sugerencia/", views.sugerencia_create, name="sugerencia"),
    path("betty's/menu/", views.menu, name="menu"),
    path("betty's/menu/agregar_platillo/", views.agregar_platillo, name="agregar_platillo"),
    path("betty's/menu/actualizar_platillo/<int:pk>", views.actualizar_platillo, name="actualizar_platillo"),
    path("betty's/menu/menu_completo/<int:pk>", views.menu_completo, name="menu_completo"),
    path("betty's/menu/eliminar_platillo/<int:pk>", views.eliminar_platillo, name="eliminar_platillo"),
    path("betty's/login/", views.CustomLoginView.as_view(), name="login"),
    path("betty's/logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("betty's/register/", views.CustomRegisterView.as_view(), name="register"),
    path("betty's/profile/", views.UpdateProfileView.as_view(), name='profile'),
    path("betty's/about/", views.about, name='about'),
]