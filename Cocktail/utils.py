import requests
import json

from Cocktail import views

def CriarPaginaInical():
    drinks_famosos = ''
    acumulador_itens_html = ''
    contador_de_elementos = 0
   

    url_base = "http://www.thecocktaildb.com/api/json/v1/1/search.php?s=" # + nome do drink 
    drinks_populares= ['Mojito']
    # drinks_populares = ['Mojito', 'Old Fashioned', 'Long Island Tea', 'Negroni', 'Whiskey Sour', 'Dry Martini','Daiquiri', 'Margarita']
    # for drink in drinks_populares:
    #     resp = requests.get(f"{url_base}{drink}")
    #     data = json.load(open(resp.json())) # <-- isso ta errado
    #     for item in data['drinks']:
    #         print(item)

    views = "index.html"
    context = {
        'drinks_famosos': drinks_famosos,

    }
    return views, context 