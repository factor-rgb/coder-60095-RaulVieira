from django.shortcuts import render

from .forms import MenuForm, CustomAuthenticationForm, CustomUserCreationForm,UserProfileForm
from .models import Foodscategories, Menu

from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.http import JsonResponse


def index(request):
      query = Foodscategories.objects.all()
      context = {"especialidades": query}
      return render(request, "core/index.html", context)

def confirmacion(request):
      return render(request, "core/confirmacion.html")


class MenuListView(ListView):
    model = Menu

    def get_menu(self):
        search = {  'Especial': 4,
                    'Sopa': 1, 
                    'Principios': 5, 
                    'Carnes': 3, 
                    'Acompañantes': 0, 
                    'Bebidas': 2,
                    }
        menu_data = {}
        for category, menu in search.items():
            data = Menu.objects.get(category=menu)
            if data.food_name:
                data.food_name = data.food_name.split(',')
            menu_data[category]= data
        return menu_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_diches'] = self.get_menu()
        return context

    def render(self, request, template, context, http_response_class, **http_response_kwargs):
        return JsonResponse(context['food_diches'])


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
            self.request, f'Inicio de Sesión Exitoso ¡Bienvenido {usuario.username}!'
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