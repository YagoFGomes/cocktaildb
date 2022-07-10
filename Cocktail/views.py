from multiprocessing import context
from django.shortcuts import render
from Cocktail.utils import CriarPaginaInical

# Create your views here.

def PaginaInicial(request):
    retorno = CriarPaginaInical()

    view = retorno[0]
    context = retorno[1]
    return render(request, view, context)