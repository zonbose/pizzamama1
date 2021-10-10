from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    '''
    pizzas_list = [pizza.name + ":" + str(pizza.price) + "$" for pizza in pizzas]
    pizzas_list_str = ", ".join(pizzas_list)'''
    return render(request, 'main/index.html')
# Create your views here.
