from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# we are telling Django that when we get to 
# http://127.0.0.1:8000/menu, we are going to be in that
# index function

# Create your views here.
def index(request):
   """ pizzas = Pizza.objects.all()
    pizzas_names_and_price= [pizza.name +' : '+str(pizza.price) +'$ ' for pizza in pizzas] # for pizza in pizzas print pizza.name=pizzas_names
    pizzas_names_and_price_str = ", ".join(pizzas_names_and_price)
    return HttpResponse('Our Pizzas : ' + pizzas_names_and_price_str )
    """
   return render(request, 'menu/index.html')
    
    
    # formatted_pizzas=[]
    
    # for pizza in pizzas:
    #     formatted_pizzas.append(f'{pizza.name}:${pizza.price}')
    # pizzas_display= ", ".join(formatted_pizzas)
    # return HttpResponse('Our Pizzas:' + pizzas_display)


#gemini i want the code to be like
# Our Pizzas: Vegetarian: $8.5, 4 cheese $6


