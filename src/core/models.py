from django.db import models


class Foodscategories(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = "categoria de comida"
        verbose_name_plural = "categorias de comidas"


class Menu(models.Model):
    food_name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Foodscategories, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='imagenes_platillos', blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return f"{self.food_name} ${self.category}"