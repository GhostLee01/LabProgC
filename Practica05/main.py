from io import open
from os import link, remove, listdir
import re
import scrapping
import weather
import xls

def getLinks(links):
    with open("links.txt") as fileLinks:
        lines = fileLinks.readlines()
        for line in lines:
            if line in links:
                continue
            line = line.split("\n")
            links.append(line[0])

    return links

def main():
    links = []
    links = getLinks(links)
    print("Esto son los link a utilizar: ")
    print("\n")
    print(links)
    print("\n")
    x = input("¿Desea agregar[s/N]?: ")
    if x == "s" or x == "S":
        links = addLinks(links)
        print("Esto son los link a utilizar: ")
        print("\n")
        print(links)
    else:
        pass
    
    print("\nBuscando información y generando archivos.")
    print("Por favor, espere.")

    #Buscar links info
    for link in links:
        match = re.findall("(wikipedia)", link)
        if match:
            wikiURL = link
    
    #Buscamos la info
    name, age, bornPlace, podiums, victories, years = scrapping.personal_info(wikiURL)

    #Buscamos sus RRSS
    socialMedia = scrapping.redes(wikiURL)

    #Buscamos link del calendario
    for link in links:
        match = re.findall("(calendar)", link)
        if match:
            calendarURL = link

    #Buscamos los siguientes eventos
    nextevents, dates = scrapping.event(calendarURL)

    #Buscar link para noticias e imágenes
    for link in links:
        match = re.findall("(noticias)", link)
        if match:
            newsUrl = link


    #Buscar las noticas
    news = scrapping.titulares(newsUrl)

    #Obtenemos las temperaturas
    temp_max_min = weather.getWeather()

    #Creamos el archivo de excel
    xls.createxls(name, age, bornPlace, socialMedia, podiums, victories, years, nextevents, dates, temp_max_min, news)

    print("\nPrograma ejecutado satisfactoriamente.\n")

    #Fin: Se le pregunta al usuario si quiere eliminar excel generado
    ls = listdir()
    for i in ls:
        match = re.findall("(\w+.xlsx)", i)
        if match:
            xlxsName = i

    x = input(f"¿Desea eliminar el archivo {xlxsName}? [s/N]: ")
    if x == "S" or x == "s":
        remove(xlxsName)
    else:
        pass


if __name__ == "__main__":
    main()
