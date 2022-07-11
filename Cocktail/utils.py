from urllib import response
import requests
import json
import random


def CriarPaginaInical():
    drinks_famosos = ''
    acumulador_itens_html = ''
    contador_de_elementos = 0
   
    url_base = "http://www.thecocktaildb.com/api/json/v1/1/search.php?s=" # + nome do drink 
    drinks_populares = ['Tequila Surprise', 'Mojito', 'Old Fashioned', 'Long Island Tea', 'Negroni', 'Whiskey Sour', 'Dry Martini','Daiquiri', 'Margarita']
    for drink in drinks_populares:
        resp = requests.get(f"{url_base}{drink}")
        response_txt = resp.json()
        lista_tags = response_txt["drinks"][0]['strTags']
        lista_de_tags = []
        if lista_tags:
            tags = lista_tags.split(',')
            if 'IBA' in tags:
                tags.remove('IBA')
            if len(tags) >= 4:
                lista_de_tags = random.sample(tags, 3)
            else: 
                lista_de_tags = tags
        lista = ''
        descricao_card = ''
        for item in lista_de_tags:
            lista += f"#{item} "
        if len(lista) == 0:
            descricao_card = """
            <p>&nbsp</p>
            """
        else: 
            descricao_card = f"""
            <p class="card-text">{lista}</p>
            """
        acumulador_itens_html += f"""
            <div class="col-sm">
                <div class="card" style="width: 18rem;">
                    <img class="card-img-top" src="{response_txt["drinks"][0]['strDrinkThumb']}"alt="{response_txt["drinks"][0]['strDrink']} image">
                    <div class="card-body">
                        <h5 class="card-title">{response_txt["drinks"][0]['strDrink']}</h5>
                        {descricao_card}
                        <a href="#" class="btn btn-primary">Confira!</a>
                    </div>
                </div>
            </div>
        """
        contador_de_elementos += 1
        if contador_de_elementos >= 3:
            drinks_famosos += f"""
                <div class="container d-flex justify-content-around mb-4">
                    {acumulador_itens_html}
                </div>
            """ 
            contador_de_elementos = 0
            acumulador_itens_html = ''

    if contador_de_elementos > 0:
        drinks_famosos += f"""
            <div class="row">
                {acumulador_itens_html}
            </div>
        """ 

    views = "index.html"
    context = {
        'drinks_famosos': drinks_famosos,

    }
    return views, context 