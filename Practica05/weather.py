#Se importan las librerias necesarias para generar nuestra API y obtener la información climatológica
import requests
import json
from datetime import datetime

def getWeather():
    #Se crean las listas donde se irán almacenando las temperaturas de los días elegidos
    Momentos = []
    Temperaturas = []
    Dias = []

    #Nuestra ID del Api de OpenWeather, generada automaticamente por la plataforma
    appid = "a3a7114576a3b54a0a02aee0bb777dea"

    #Generamos el link de nuestra ciudad y aplicamos el método request.get para hacer la solicitud http a OpenWeather
    page=requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat=41.389&lon=2.159&exclude=minutely,hourly&units=metric&appid=a3a7114576a3b54a0a02aee0bb777dea")
    #print()

    #Aplicamos page.status_code para que podamos apreciar que código de respuesta obtenemos de nuestra solicitud
    #En nuestro caso buscamos que sea código 200 el cual representa que todo está en orden 
    #print(f"The code of the request is: {page.status_code}")

    #Convertimos la cadena JSON obtenida en un diccionario de Python utilizando el método json.loads()
    Clima_INFO = json.loads(page.content)

    #Buscaremos en todo el diccionario obtenido en el paso anterior
    for x, y in Clima_INFO.items():
        #Buscamos donde comienza la información de temperaturas de cada día, esto se sabe pues 
        #Cada día diferente inicia con la clave "daily"
        if x == "daily":
            
            #Damos el rango para poder imprimir los días que buscamos, en este caso buscamos del 20 al 22 de Mayo
            for i in y[1:5]:
                Fecha = int(i['dt'])
                #El metodo datetime obtiene la fecha actual, y el metodo strftime le dará formato a dicha fecha, pues 
                #Convierte una tupla generada en una cadena, que será nuestra fecha en formato aaaa/mm/dd
                Actual = datetime.utcfromtimestamp(Fecha).strftime("%Y-%m-%d")
                Dias.append(Actual)
                #Key representa la parte del día que se esta buscando, ejemplo: Morning, Evening, Night, por eso 
                #se añadiran a la lista listakey que teniamos al principio, la cual contendrá dichas etiquetas 
                #que serán vaciadas en el excel más adelante
                for key in i['temp']:
                    Momentos.append(key)
                    
                    #Se comienza a llenar nuestra lista de temperaturas

                    #Se busca las que coincidan con el día y se añaden a Temperaturas
                    Temperaturas.append(i['temp']['day'])
                    #Se busca las que coincidan con la tarde y se añaden a Temperaturas
                    Temperaturas.append(i['temp']['eve'])
                    #Se busca las que coincidan con la noche y se añaden a Temperaturas
                    Temperaturas.append(i['temp']['night'])
                    #Se busca las que coincidan con la minima y se añaden a Temperaturas
                    Temperaturas.append(i['temp']['min'])
                    #Se busca las que coincidan con la maxima y se añaden a Temperaturas
                    Temperaturas.append(i['temp']['max'])

    #Se imprimen los resultados
    '''
    print(f"El patron de resultados es el siguiente: {Momentos}")
    print("---------------")
    print(Temperaturas)
    print("---------------")
    print(f"Los días obtenidos son:  {Dias}")
    print("---------------")'''

    temp_max_min = {"d1":[Temperaturas[1], Temperaturas[2]], 
    "d2":[Temperaturas[7], Temperaturas[8]], 
    "d3":[Temperaturas[14], Temperaturas[13]],
    "d4":[Temperaturas[19], Temperaturas[20]]}

    return temp_max_min