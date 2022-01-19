import time
import datetime as dt

import logicaDeNegocio

def traerContenidoALista():
    f = open("ListadoDeAcciones.txt")
    contenido = f.read()
    listaDeAcciones = contenido.split()
    return listaDeAcciones

def cierreDelPrograma():
    print("Adios")
    time.sleep(1)
    exit(0)
  
def agregarAccion(ticker):
    listaDeAcciones = traerContenidoALista()
    setDeAcciones = set(listaDeAcciones)
    setDeAcciones.add(ticker)
    listaDeAcciones = list(setDeAcciones)
    f = open("ListadoDeAcciones.txt" , "w")

    for x in listaDeAcciones:
        with open('ListadoDeAcciones.txt' , 'a') as f:
            f.write(x)
            f.write("\n")

def removerAccion(accion):
    listaDeAcciones = traerContenidoALista()
    try:
        listaDeAcciones.remove(accion)
    except:
        print("Esa accion no existe")
        return 0

    for x in listaDeAcciones:
        agregarAccion(x)

def listarAcciones():
    listaDeAcciones = traerContenidoALista()

    print("----")
    for x in listaDeAcciones:
        print(x)
    print("----")

def simular():

    print("ingrese la fecha de inicio en formato yyyy-mm-dd")
    start_str = input()
    start = dt.datetime.strptime(start_str, '%Y-%m-%d').date()
    print("ingrese la fecha de fin en formato yyyy-mm-dd")
    end_str= input()
    end = dt.datetime.strptime(end_str, '%Y-%m-%d').date()


    logicaDeNegocio.ChequearAcciones(start , end)



def default():
   return "Opcion Invalida"

def menu(): 
    print("-----------   Menu   --------------")
    print("1. Agregar accion")
    print("2. Eliminar accion")
    print("3. Ver listado de acciones")
    print("4. Simular el programa dada una fecha")
    print("0. Finalizar programa")
    print("-----------------------------------")

def switch(accion):
    if accion == 0:
        cierreDelPrograma()

    elif accion == 1:
            print("\n Ingrese el ticker de la accion sin espacios y con mayusculas (ejemplo: AAPL) \n")
            ticker = input()
            agregarAccion(ticker)

    elif accion == 2:
        print("\n Ingrese el ticker de la accion que quiera eliminar de la siguiente lista \n")
        listarAcciones()
        ticker = input()
        removerAccion(ticker)

    elif accion == 3:
        listarAcciones()

    elif accion == 4:
        simular()
    else:
        print("opcion invalida")
        return -1

while 1:
    
    menu()
    accion = int(input())
    switch(accion)


