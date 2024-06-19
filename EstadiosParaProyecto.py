#traer herramientas necesarias
import requests 
import bs4
#colocar la página que quiero mostrar y luego cargarla en requests
def estadiosDeLaEurocopa():
    contador = 1
    pagina = "https://www.sportingnews.com/us-es/futbol/news/eurocopa-2024-estadios-sedes/93b6d3c3324061b17d8e001d"
    pagina = requests.get (pagina).text
    #pasarla a BeautifulSoup
    soup = bs4.BeautifulSoup(pagina,"html.parser")
    #(soup)
    #buscar todas las etiquetas a
    etiquetas = soup.find_all ("h3")
    for x in etiquetas:
        if "Edition" in x.text:
            print (" ")
        else:
            print (contador, end = ". ")
            contador += 1
            print (x.text)