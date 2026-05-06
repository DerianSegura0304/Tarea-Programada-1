#Programa Principal / Menu tarea principal
# Elaborado por: Gabriel Josue Marin Munoz y Derian Segura
# Fecha de elaboración: 25/04/2026 10:10 am
# fecha de última actualización: 01/05/2026 9:44pm
#version de python: 3.14.3

#Variables Globales
listaEquivalencias = []

#Importaciones
import funciones
import csv

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
        funciones.registrarAccion("El usuario selecciono la opcion 1: En donde cargara los tokens que tenga en sus archivos")
        
    elif letraProceso == "2":                                      
        print("Lectura de tokens \n")
        funciones.mostrarTokens(listaEquivalencias)
        funciones.registrarAccion("El usuario selecciono la opcion 2: En donde mostrara en una tabla los tokens cargados")
    elif letraProceso == "3":
        print("Agregar o modificar Tokens \n")
        nuevosTokens = input("Antes de digitar sus nuevos tokens, por favor separelos con un + de la siguiente manera:\ntoken =(su separador) equivalencia + token = equivalencia + ...\n\nDigite sus nuevos tokens: ")
        nuevoSeparador = input("Digite su separador de sus nuevos tokens: ")
        print(funciones.agregarModificarTokensAux(nuevosTokens, nuevoSeparador, listaEquivalencias))
        funciones.registrarAccion("El usuario selecciono la opcion 3: En donde podra agregar o modificar tokens previamente cargados")
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
        funciones.registrarAccion("El usuario selecciono la opcion 4: En Donde  guardara los tokens en un archivo")

    elif letraProceso == "5":
        nombreArchivo = input("\nIntroduzca el nombre y formato de su archivo a leer, como en el siguiente ejemplo5: archivo.txt\n\nDigite el nombre de su archivo: ")
        resultadoTraduccion = funciones.traducirCodigo(nombreArchivo, listaEquivalencias)
        print(resultadoTraduccion)
        funciones.registrarAccion("El usuario selecciono la opcion 5: En donde Traducira codigo con los tokens guardados")

    elif letraProceso == "6":
        print("Generar reporte csv \n")
        nombreCsv = input("digite el nombre del archivo csv en donde usted quiere generar el reporte. (ejemplo: reporte1)")
        mensaje = funciones.generarReporteCvs(nombreCsv, resultadoTraduccion, listaEquivalencias)
        print(mensaje)
        funciones.registrarAccion("El usuario selecciono la opcion 6: En donde  generara un reporte csv en un archivo antes creado por el usuario")
    elif letraProceso == "7":
        print("Generar archivo html \n")
        funciones.registrarAccion("El usuario selecciono la opcion 7: En donde el usuario generara un archivo html .")
    elif letraProceso == "8":
        print("Submenu de bitacora del sistema \n")
        eleccionBitacora = input("Digite el numero del proceso que desea realizar\n1 - acciones día escogido\n2 - Acciones con algunas palabras clave\n3 - Salir del submenu de bitacora\nDigite su numero: ")
        if eleccionBitacora == "1":
            print("Acciones día escogido \n")
            datosBitacora = funciones.obtenerBitacora()
        
        if not datosBitacora:
            print("\n[!] La bitácora está vacía o el archivo no existe aún.")
        else:
            continuarDos = True
            while continuarDos:
                print("\nOpciones de búsqueda:")
                print("1 - Buscar registros por fecha (AAAA-MM-DD)")
                print("2 - Buscar por palabra clave en la descripción")
                print("3 - Volver al menú principal")
                eleccionBitacora = input("\nSeleccione su opción: ")
                if eleccionBitacora == "1":
                    print("\n-- Búsqueda por Fecha --")
                    fecha_busqueda = input("Digite la fecha (ejemplo: 2026-05-01): ")
                    encontrado = False
                    print("-" * 50)
                    for registro in datosBitacora:
                        if fecha_busqueda in registro[0]:
                            print(f"Fecha: {registro[0]} | Acción: {registro[1]}")
                            encontrado = True
                    if not encontrado:
                        print("No se encontraron registros para esa fecha.")
                    print("-" * 50)
                elif eleccionBitacora == "2":
                    print("\n-- Búsqueda por Palabra Clave --")
                    palabra = input("Digite la palabra o frase a buscar: ").lower()
                    encontrado = False
                    print("-" * 50)
                    for registro in datosBitacora:
                        if palabra in registro[1].lower():
                            print(f"Fecha: {registro[0]} | Acción: {registro[1]}")
                            encontrado = True
                    if not encontrado:
                        print(f"No hay registros que contengan: '{palabra}'")
                    print("-" * 50)
                elif eleccionBitacora == "3":
                    print("Saliendo del submenú de bitácora...")
                    continuarDos = False
                else:
                    print("Opción no válida. Intente de nuevo.")
    elif letraProceso == "9":
        print("Salir del programa \n")
        continuar = False
    else:
        print("Digitaste un numero diferente de 1, 2, 3, 4, 5, 6, 7, 8 y 9... Regresando al menu\n")
