from django.contrib import admin

# Register your models here.
from .models import Menu,CategoriasComidas

# admin.site.register(CategoriasComidas)
# admin.site.register(Menu)

@admin.register(CategoriasComidas)
class CategoriasComidasAdmin(admin.ModelAdmin):
    list_display = ("categoria",)
    search_fields = ("categoria",)
    ordering = ("categoria",)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("platillo", "imagen", "categoria_comida", "precio")
    search_fields = ("platillo", "categoria_comida")
    ordering = ("platillo", "categoria_comida", "precio")
    list_filter = ("categoria_comida",)