from django.shortcuts import redirect,render

from django.http import HttpRequest, HttpResponse
from .models import Categorias_Comidas, Menu
from .forms import PedidosForm, ReservacionesForm, Suerencias_ComidasForm, MenuForm


def index(request):
      query = Categorias_Comidas.objects.all()
      context = {"especialidades": query}
      return render(request, "core/index.html", context)


def confirmacion(request):
      return render(request, "core/confirmacion.html")


def pedido_create(request: HttpRequest) -> HttpResponse:
      if request.method == "GET":
            form = PedidosForm()
      if request.method == "POST":
            form = PedidosForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect("core:confirmacion")
      return render(request,"core/pedido_form.html", {"form": form})


def reservacion_create(request: HttpRequest) -> HttpResponse:
      if request.method == "GET":
            form = ReservacionesForm()
      if request.method == "POST":
            form = ReservacionesForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect("core:confirmacion")
      return render(request,"core/reservacion_form.html", {"form": form})


def sugerencia_create(request: HttpRequest) -> HttpResponse:
      if request.method == "GET":
            form = Suerencias_ComidasForm()
      if request.method == "POST":
            form = Suerencias_ComidasForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect("core:confirmacion")
      return render(request,"core/sugerencia_form.html", {"form": form})


def menu(request: HttpRequest) -> HttpResponse:
    busqueda = request.GET.get('busqueda')
    if busqueda:
        queryset = Menu.objects.filter(platillo__icontains=busqueda)
    else:
        queryset = Menu.objects.all()
    return render(request, 'core/menu.html', {'object_list': queryset})


def agregar_platillo(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = MenuForm()
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:confirmacion')
    return render(request, 'core/agregar_platillo.html', {'form': form})


def actualizar_platillo(request: HttpRequest, pk: int) -> HttpResponse:
    query = Menu.objects.get(id=pk)
    if request.method == 'GET':
        form = MenuForm(instance=query)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('core:confirmacion')
    return render(request, 'core/agregar_platillo.html', {'form': form})


def menu_completo(request: HttpRequest, pk: int) -> HttpResponse:
    query = Menu.objects.get(id=pk)
    return render(request, 'core/menu_completo.html', {'object': query})


def eliminar_platillo(request: HttpRequest, pk: int) -> HttpResponse:
    query = Menu.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('core:menu')
    return render(request, 'core/eliminar_platillo.html', {'object': query})