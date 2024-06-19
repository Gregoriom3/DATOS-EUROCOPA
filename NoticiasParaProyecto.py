import requests 
import bs4
def esNoticia (x):
     if x != "EUROCOPA 2024" and len (x) != 0 and x [0] != " " and len (x.strip()) > 15 and not x.isupper() and "  " not in x and x != "Todos los resultados" and x != "Video En Directo" and "Vídeos de la Eurocopa" not in x and x.strip().count ("\n") < 4:
            return True
     else:
         return False
#traer herramientas necesarias
#colocar la página que quiero mostrar y luego cargarla en requests
def sacarNoticias():
    contador = 1
    pagina = "https://as.com/futbol/eurocopa/"
    pagina = requests.get (pagina).text
    #pasarla a BeautifulSoup
    soup = bs4.BeautifulSoup(pagina,"html.parser")
    #(soup)
    #buscar todas las etiquetas img y +
    etiquetas = soup.find_all ("a")
    etiquetas [1:15]
    for x in etiquetas:
        if esNoticia (x.text):
             print (contador,end = ". ")
             contador += 1
             print (x.text)