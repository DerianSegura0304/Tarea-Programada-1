#Programa Principal / Menu tarea principal
# Elaborado por: Gabriel Josue Marin Munoz y Derian Segura
# Fecha de elaboración: 25/04/2026 10:10 am
# fecha de última actualización: 25/04/2026 6:25pm
#version de python: 3.14.3

#Variables Globales
listaEquivalencias = []

#Importaciones
import re
import csv
import funciones

# menú
continuar = True 
while  continuar:
    print("-" * 75)                        
    print("\nDigite un numero segun el proceso deseado\n\n1 - Procesar carga de tokens\n2 - Lectura de Tokens \n3 - Agregar o modificar Tokens \n4 - Guardar Tokens en archivo \n5 - Traducir codigo \n6 - Generar reporte csv\n7 - Generar archivo html\n8 - Submenu de bitacora del sistema\n9 - Salir del programa")
    letraProceso = input("\nDigite su numero: ")                    
    print("-" * 75) 
    if letraProceso == "1":                                   
        print("Procesar carga de tokens\n")    
        nombreArchivoTokens = input("Digite el nombre de su archivo que contenga sus tokens junto con su formato, ejemplo: .txt: ") 
        metodoSeparacion = input('\nMetodos de separacion y su numero:\n1: "->"\n2: ","\n3: "="\n\nDigite el numero: ')
        if metodoSeparacion == "1":
            metodoSeparacion = "->"
        elif metodoSeparacion == "2":
            metodoSeparacion = ","
        elif metodoSeparacion == "3":
            metodoSeparacion = "="
        else:
            print("Digito un numero distinto de 1, 2 o 3")
            continue
        listaEquivalencias = funciones.cargarTokens(nombreArchivoTokens, metodoSeparacion, listaEquivalencias)
        print(listaEquivalencias)
        
    elif letraProceso == "2":                                      
        print("Lectura de tokens \n")
        funciones.mostrarTokens(listaEquivalencias)
    elif letraProceso == "3":
        print("Agregar o modificar Tokens \n")
        nuevosTokens = input("Antes de digitar sus nuevos tokens, por favor separelos con un + de la siguiente manera:\ntoken =(su separador) equivalencia + token = equivalencia + ...\n\nDigite sus nuevos tokens: ")
        nuevoSeparador = input("Digite su separador de sus nuevos tokens: ")
        print(funciones.agregarModificarTokens(nuevosTokens, nuevoSeparador, listaEquivalencias))
    elif letraProceso == "4":
        print("Guardar tokens en un archivo \n")
        nombreArchivoGuardar = input("Digite el nombre del archivo donde desea guardar sus tokens junto con su formato, ejemplo: .txt: ")
        metodoSeparacion = input('\nMetodos de separacion y su numero:\n1: "->"\n2: ","\n3: "="\n\nDigite el numero: ')
        if metodoSeparacion == "1":
            metodoSeparacion = "->"
        elif metodoSeparacion == "2":
            metodoSeparacion = ","
        elif metodoSeparacion == "3":
            metodoSeparacion = "="
        else:
            print("Digito un numero distinto de 1, 2 o 3")
            continue
        resultado = funciones.guardarTokens(nombreArchivoGuardar, metodoSeparacion, listaEquivalencias)
        print("\n" + resultado)
    elif letraProceso == "5":
        print("Traducir codigo \n")
    elif letraProceso == "6":
        print("Generar reporte csv \n")
    elif letraProceso == "7":
        print("Generar archivo html \n")
    elif letraProceso == "8":
        print("Submenu de bitacora del sistema \n")
        eleccionBitacora = input("Digite el numero del proceso que desea realizar\n1 - acciones día escogido\n2 - Acciones con algunas palabras clave\n3 - Salir del submenu de bitacora\nDigite su numero: ")
        if eleccionBitacora == "1":
            print("Acciones día escogido \n")
        elif eleccionBitacora == "2":
            print("Acciones con algunas palabras clave \n")
        elif eleccionBitacora == "3":
            print("Salir del submenu de bitacora \n")
        else:
            print("Digitaste un numero diferente de 1, 2 y 3... Regresando al menu\n")
    elif letraProceso == "9":
        print("Salir del programa \n")
        continuar = False
    else:
        print("Digitaste un numero diferente de 1, 2, 3, 4, 5, 6, 7, 8 y 9... Regresando al menu\n")
