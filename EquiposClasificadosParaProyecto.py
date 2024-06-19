#traer herramientas necesarias
import requests 
import bs4
#colocar la página que quiero mostrar y luego cargarla en requests
def equiposClasificados():
    contador = 1
    pagina = "https://www.goal.com/es-co/noticias/que-equipos-estan-clasificados-para-la-eurocopa-2024/bltaccbb32e597c225a"
    pagina = requests.get (pagina).text
    #pasarla a BeautifulSoup
    soup = bs4.BeautifulSoup(pagina,"html.parser")
    #(soup)
    #buscar todas las etiquetas a
    etiquetas = soup.find_all ("h2")
    for x in etiquetas:
        print (contador, end = ". ")
        contador += 1
        print (x.text)