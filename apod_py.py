#Otbteniendo la imagen astrónomica del día (Astronomic Picture Of the Day) mediante una API de la NASA: https://api.nasa.gov/planetary/apod?
#APOD -> APOD es un servicio que nos provee una imagen astronómica diaria, ademas de la imagen, nos proporciona una breve descripción de esta.

import requests
import webbrowser #Webbrowser sirve para que algún link/url/ruta al ser recibida pueda abrirse y ser redirigida al navegador de mi sistema.

#Pido al usuario una fecha en específico para la foto con el formato  AÑO-MES-DÍA:
date = input('Ingrese una fecha en formato AÑO-MES-DÍA: ')

#Parámetros que se pasarán a la API al realizarse la petición, la KEY y la fecha de la imagen introducida por el usuario.
params = {'api_key': 'DEMO_KEY', "date": date}

print(f'Obteniendo imágen de la fecha {params["date"]}')

#Realizo la petición a la API de la NASA:
r = requests.get('https://api.nasa.gov/planetary/apod?', params=params)

#Obtengo el doc JSON:
json_doc = r.json()
#print(json_doc)

#Ahora se deberá realizar una condición. Si el archivo es una imagen, se descargará en mi PC, de lo contrario, si es un vídeo me redirigirá a mi navegador:
if json_doc['media_type'] == 'image':
    #Realizo nuevamente una petición a la API pero esta vez con la URL de la imagen de la fecha:
    img_url = requests.get(json_doc['url'])

    #Guardo en una variable la descripción de la imagen:
    img_text = json_doc['explanation']

    #Creo y Descargo mi archivo .txt con la descripción de la foto:
    with open('APOD-DESCRIPTION-' + params['date'] + '.txt', 'w') as archivo:
        for line in img_text:
            archivo.write(line)

    #Creo y Descargo mi archivo .jpg:
    with open('APOD-IMAGE' + params['date'] + '.jpg', 'wb') as archivo:
        for chunk in img_url.iter_content():
            archivo.write(chunk)
        
        print('\n Imágen APOD-' + params['date'] + '.jpg ha sido descargado CORRECTAMENTE')

else: #Para el vídeo:
    webbrowser.open_new_tab(json_doc['url'])