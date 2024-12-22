from django.shortcuts import render

from .forms import PedidosForm, ReservacionesForm, Suerencias_ComidasForm, MenuForm, CustomAuthenticationForm, CustomUserCreationForm,UserProfileForm
from .models import Categorias_Comidas, Menu, Pedidos, Reservaciones, Sugerencias_Comidas

from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.forms import BaseModelForm
from django.urls import reverse_lazy


def index(request):
      query = Categorias_Comidas.objects.all()
      context = {"especialidades": query}
      return render(request, "core/index.html", context)


def about(request):
      return render(request, "core/about.html")


def confirmacion(request):
      return render(request, "core/confirmacion.html")


class PedidoCreateView(CreateView):
    model = Pedidos
    form_class = PedidosForm
    success_url = reverse_lazy('core:confirmacion')


class ReservacionCreateView(CreateView):
    model = Reservaciones
    form_class = ReservacionesForm
    success_url = reverse_lazy('core:confirmacion')


class SugerenciaCreateView(CreateView):
    model = Sugerencias_Comidas
    form_class = Suerencias_ComidasForm
    success_url = reverse_lazy('core:confirmacion')


class MenuListView(ListView):
    model = Menu

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda')
        if busqueda:
            return Menu.objects.filter(platillo__icontains=busqueda)
        return Menu.objects.all()


class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    success_url = reverse_lazy('core:confirmacion')


class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    success_url = reverse_lazy('core:confirmacion')


class MenuDetailView(DetailView):
    model = Menu


class MenuDeleteView(DeleteView):
    model = Menu
    success_url = reverse_lazy('core:menu')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'
    next_page = reverse_lazy('core:index')

    def form_valid(self, form: AuthenticationForm):
        usuario = form.get_user()
        messages.success(
            self.request, f'Inicio de sesión exitoso ¡Bienvenido {usuario.username}!'
        )
        return super().form_valid(form)


class CustomRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login')

    def form_valid(self, form: BaseModelForm):
        messages.success(self.request, 'Usuario Registrado con Exito')
        return super().form_valid(form)


class UpdateProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'core/profile.html'
    success_url = reverse_lazy('core:confirmacion')

    def get_object(self):
        return self.request.user
