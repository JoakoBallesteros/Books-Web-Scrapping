import time
import bs4
import requests

# crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    
    # verificar si la página se cargó correctamente
    if resultado.status_code == 200:
        sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')
    else:
        print(f'Error al cargar la página {url_pagina}')
        continue

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # chequear que tengan 4 o 5 estrellas
        if 'star-rating' in libro.select('p')[0]['class']:
            rating = libro.select('p')[0]['class'][1]
            if rating in ['Four', 'Five']:
                # guardar titulo en variable
                titulo_libro = libro.select('h3 a')[0]['title']

                # agregar libro a la lista
                titulos_rating_alto.append(titulo_libro)
    # esperar 2 segundos antes de hacer la siguiente solicitud (para evitar sobrecargar el servidor)
    time.sleep(2)

# ver libros 4 u 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)
