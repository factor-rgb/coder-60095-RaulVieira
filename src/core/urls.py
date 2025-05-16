from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("betty's/confirmacion/", views.confirmacion, name="confirmacion"),
    path("betty's/menu/", views.MenuListView.as_view(), name="menu"),
    path("betty's/menu/agregar_platillo/", views.MenuCreateView.as_view(), name="agregar_platillo"),
    path("betty's/menu/actualizar_platillo/<int:pk>", views.MenuUpdateView.as_view(), name="actualizar_platillo"),
    path("betty's/menu/menu_completo/<int:pk>", views.MenuDetailView.as_view(), name="menu_completo"),
    path("betty's/menu/eliminar_platillo/<int:pk>", views.MenuDeleteView.as_view(), name="eliminar_platillo"),
    path("betty's/login/", views.CustomLoginView.as_view(), name="login"),
    path("betty's/logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("betty's/register/", views.CustomRegisterView.as_view(), name="register"),
    path("betty's/profile/", views.UpdateProfileView.as_view(), name='profile'),
]