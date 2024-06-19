from NoticiasParaProyecto import sacarNoticias 
from EquiposClasificadosParaProyecto import equiposClasificados
from EstadiosParaProyecto import estadiosDeLaEurocopa
from MarcadoresParaProyecto import marcadoresDeLosPartidos
print (""" 
 ______        _     _________    ___     ______         ________  _____  _____  _______      ___      ______    ___   _______     _       
|_   _ `.     / \   |  _   _  | .'   `. .' ____ \       |_   __  ||_   _||_   _||_   __ \   .'   `.  .' ___  | .'   `.|_   __ \   / \      
  | | `. \   / _ \  |_/ | | \_|/  .-.  \| (___ \_|        | |_ \_|  | |    | |    | |__) | /  .-.  \/ .'   \_|/  .-.  \ | |__) | / _ \     
  | |  | |  / ___ \     | |    | |   | | _.____`.         |  _| _   | '    ' |    |  __ /  | |   | || |       | |   | | |  ___/ / ___ \    
 _| |_.' /_/ /   \ \_  _| |_   \  `-'  /| \____) |       _| |__/ |   \ \__/ /    _| |  \ \_\  `-'  /\ `.___.'\\  `-'  /_| |_  _/ /   \ \_  
|______.'|____| |____||_____|   `.___.'  \______.'      |________|    `.__.'    |____| |___|`.___.'  `.____ .' `.___.'|_____||____| |____|                                                                                                                           
       """)
while True:
    print ()
    print ("1.mostrar noticias")
    print ("2.mostrar estadios")
    print ("3.mostrar marcadores")
    print ("4.mostrar equipos clasificados")
    print ("5.salir")
    opcion = input ("¿Cuál opción quiero?")
    if opcion == "1":
        print ("mostrar noticias")
        sacarNoticias()
    elif opcion == "2":
        print ("mostrar estadios de la eurocopa")
        estadiosDeLaEurocopa()
    elif opcion == "3":
        print ("mostrar marcadores de los partidos")
        marcadoresDeLosPartidos()
    elif opcion == "4":
        print ("mostar equipos clasificados")
        equiposClasificados()
    elif opcion == "5":
        print ("salir")
        break
    else:
        print("opción no válida")