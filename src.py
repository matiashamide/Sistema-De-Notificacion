import time


def cierreDelPrograma():
    print("Adios")
    time.sleep(1)
    exit(0)
  
def funcion1():
    print("anashe")
    return 0
def funcion2():
    return 0
def funcion3():
    return 0
def default():
   return "Opcion Invalida"

def switch(accion):
    match accion:
        case 0:
            cierreDelPrograma()
        case 1:
            return 0
        case 2:
            return 0
        case 3:
            return 0
        case 4:
            return 0
        case _:
            print("opcion invalida")
            return -1

'''
def switch(case):
   sw = {
      1: funcion1(),
      2: funcion2(),
      3: funcion3(), 
      9: cierreDelPrograma(),
   }
   return sw.get(case, default())
'''

def menu():
    print("----------- Calculadora -----------")
    print("0. Finalizar programa")
    print("1. Agregar accion")
    print("2. Eliminar accion")
    print("3. Ver listado de acciones")
    print("4. indefinido") 
   
    print("-----------------------------------")

while 1:
    print("que quiere hacer")
    menu()

    accion = int(input())
    switch(accion)


