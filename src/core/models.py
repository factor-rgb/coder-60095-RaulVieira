from django.db import models


class CategoriasComidas(models.Model):
    categoria = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.categoria


class Menu(models.Model):
    platillo = models.CharField(max_length=255, unique=True)
    categoria_comida = models.ForeignKey(CategoriasComidas, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='imagenes_platillos', blank=True, null=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.platillo} ${self.precio}"