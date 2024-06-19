#traer herramientas necesarias
import requests 
import bs4
#colocar la página que quiero mostrar y luego cargarla en requests
def marcadoresDeLosPartidos():
    yaPasoPorElGrupoA = False
    pagina = "https://resultados.as.com/resultados/futbol/eurocopa/2024/jornada/"
    pagina = requests.get (pagina).text
    #pasarla a BeautifulSoup
    soup = bs4.BeautifulSoup(pagina,"html.parser")
    #(soup
    #buscar todas las etiquetas a
    etiquetas = soup.find_all ("a")
    for x in etiquetas:
        #print (x.text.strip().replace("  ",""))
        if "Grupo A" in x.text:
            yaPasoPorElGrupoA = True
        if yaPasoPorElGrupoA == True:
            if "Resultados" not in x.text:
                print (x.text.strip().replace("  ",""))
            else:
                break