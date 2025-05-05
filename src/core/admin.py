from django.contrib import admin

# Register your models here.
from .models import Menu,Foodscategories

# admin.site.register(CategoriasComidas)
# admin.site.register(Menu)

@admin.register(Foodscategories)
class FoodscategoriesAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    search_fields = ("category_name",)
    ordering = ("category_name",)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("food_name", "image", "category", "price")
    search_fields = ("food_name", "category")
    ordering = ("food_name", "category", "price")
    list_filter = ("category",)