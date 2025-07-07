from django.contrib import admin


# Register your models here.
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display=('name', 'ingredients', 'vegetarian', 'price')
    search_fields=['name']

admin.site.register(Pizza, PizzaAdmin)