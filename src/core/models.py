from django.db import models


class Categorias_Comidas(models.Model):
    categoria = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.categoria


class Menu(models.Model):
    platillo = models.CharField(max_length=255, unique=True)
    categoria_Comida = models.ForeignKey(Categorias_Comidas, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.platillo} - {self.categoria_Comida}"


class Sugerencias_Comidas(models.Model):
    sugerencia = models.CharField(max_length=255)
    categoria_comida = models.ForeignKey(Categorias_Comidas, on_delete=models.SET_NULL, null=True)


class Reservaciones(models.Model):
    nombre = models.CharField(max_length=255)
    reservacion_fecha = models.DateField()


class Pedidos(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    platillo = models.ForeignKey(Menu, on_delete=models.CASCADE)
