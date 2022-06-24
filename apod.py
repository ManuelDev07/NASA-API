#Otbteniendo la imagen o vídeo astrónomico del día (Astronomic Picture Of the Day) mediante APIs Públicas de la NASA: https://api.nasa.gov/index.html#getting-started
#APOD -> APOD es un servicio que nos provee un vídeo o imágen astronómico, ademas del archivo, también nos proporciona una breve descripción de este.

import requests
import webbrowser #Webbrowser sirve para que algún link/url/ruta al ser recibida pueda abrirse y ser redirigida al navegador de mi sistema.

#Pido al usuario una fecha en específico para la foto con el formato  AÑO-MES-DÍA:
date = input('Ingrese una fecha en formato AÑO-MES-DÍA: ')

#Parámetros que se pasarán a la API al realizarse la petición, la KEY y la fecha de la imagen introducida por el usuario.
params = {'api_key': 'DEMO_KEY', "date": date}

print(f'Obteniendo datos de la fecha: {params["date"]}')

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
        
        print('\n Descripción APOD-' + params['date'] + '.txt ha sido descargado CORRECTAMENTE')

    #Creo y Descargo mi archivo .jpg:
    with open('APOD-IMAGE-' + params['date'] + '.jpg', 'wb') as archivo:
        for chunk in img_url.iter_content():
            archivo.write(chunk)
        
        print('\n Imágen APOD-' + params['date'] + '.jpg ha sido descargado CORRECTAMENTE')

else: #Para el vídeo:
    #Realizo una petición a la API pero esta vez será para obtener el vídeo:
    video_url = requests.get(json_doc['url'])

    #Guardo en una variable la descripción de la imagen:
    video_text = json_doc['explanation']

    #Creo y Descargo mi archivo .txt con la descripción de la foto:
    with open('APOD-DESCRIPTION-' + params['date'] + '.txt', 'w') as archivo:
        for line in video_text:
            archivo.write(line)
        
        print('\n Descripción APOD-' + params['date'] + '.txt ha sido descargado CORRECTAMENTE')

    #Creo y Descargo mi archivo como .mp4:
    with open('APOD-VIDEO-' + params['date'] + '.mp4', 'wb') as archivo:
        for chunk in video_url.iter_content():
            archivo.write(chunk)
        
        print('\n Vídep APOD-' + params['date'] + '.mp4 ha sido descargado CORRECTAMENTE')
