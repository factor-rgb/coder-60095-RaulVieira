from django.shortcuts import redirect,render

from .models import Categorias_Comidas
from .forms import PedidosForm, ReservacionesForm, Suerencias_ComidasForm


def index(request):
      query = Categorias_Comidas.objects.all()
      context = {"especialidades": query}
      return render(request, "core/index.html", context)


def confirmacion(request):
      return render(request, "core/confirmacion.html")


def pedido_create(request):
      if request.method == "GET":
            form = PedidosForm()
      if request.method == "POST":
            form = PedidosForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect("core:confirmacion")
      return render(request,"core/pedido_form.html", {"form": form})


def reservacion_create(request):
      if request.method == "GET":
            form = ReservacionesForm()
      if request.method == "POST":
            form = ReservacionesForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect("core: confirmacion")
      return render(request,"core/reservacion_form.html", {"form": form})


def sugerencia_create(request):
      if request.method == "GET":
            form = Suerencias_ComidasForm()
      if request.method == "POST":
            form = Suerencias_ComidasForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect("core:confirmacion")
      return render(request,"core/sugerencia_form.html", {"form": form})