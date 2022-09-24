from multiprocessing import context
from django.shortcuts import render
from Cocktail.utils import CriarPaginaInical, CriarPaginaDrinks

# Create your views here.

def PaginaInicial(request):
    retorno = CriarPaginaInical()

    view = retorno[0]
    context = retorno[1]
    return render(request, view, context)

def DrinksAlcoolicos(request, tipo):
    retorno = CriarPaginaDrinks()

    view = retorno[0]
    context = retorno[1]

    return render(request, view, context)

