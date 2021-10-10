from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request):
    '''
    pizzas_list = [pizza.name + ":" + str(pizza.price) + "$" for pizza in pizzas]
    pizzas_list_str = ", ".join(pizzas_list)'''
    pizzas = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', {'pizzas': pizzas})
