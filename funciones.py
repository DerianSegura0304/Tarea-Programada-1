#importaciones
def cargarTokens(nombreArchivoTokens, metodoSeparacion, listaEquivalencias):
    """
    Función: Lee un archivo de texto con tokens, los separa según el método indicado y los almacena en una lista. 
    Si un token ya existe, lo reescribe con el nuevo valor para mantener la versión más reciente.
    Entradas:
    -nombreArchivoTokens(str): Nombre del archivo físico que contiene los tokens y sus equivalencias.
    -metodoSeparacion(str): Carácter separador que divide el token de su significado, ejemplo: "->", "=", ",".
    -listaEquivalencias(list): Lista que almacena las tuplas de los tokens cargados actualmente.
    Salidas:
    -listaEquivalencias(list): Lista retornada con todas las tuplas nuevas y las reescritas procesadas.
    -Mensaje de error(str): Texto retornado en caso de que el archivo no sea localizado por el sistema.
    """
    try:
        archivo = open(nombreArchivoTokens, "r")                         #Se abre el archivo en modo lectura "r" para extraer los datos
        print("\nleyendo el archivo...\n")
        for linea in archivo:                                            #Inicia un ciclo para procesar cada una de las líneas del documento
            linea = linea.strip("\n")                                    #Se elimina el salto de línea al final del texto para limpiar el dato
            linea = linea.split(metodoSeparacion)                        #Divide la hilera en partes según el separador indicado por el usuario
            linea = tuple(linea)                                         #Convierte el par de datos en una tupla para cumplir con el formato de almacenamiento
            encontrado = False                                           #Bandera que ayuda a determinar si el token es nuevo o una reescritura
            for tupla in range(len(listaEquivalencias)):                 #Ciclo que recorre los índices de la lista para buscar coincidencias
                if linea[0] == listaEquivalencias[tupla][0]:             
                    print(f"Se reescribió {linea[0]}, y conservará el reemplazo más reciente.") #Notifica al usuario sobre la sustitución del valor
                    listaEquivalencias[tupla] = linea                    #Reemplaza la tupla vieja por la nueva en la posición exacta encontrada
                    encontrado = True                                    #Marca como encontrado para no agregar el token como si fuera nuevo
                    break                                                #Sale del ciclo de búsqueda al haber logrado el reemplazo
            if not encontrado:                                           
                listaEquivalencias.append(linea)                         #Agrega la nueva tupla al final de la lista de equivalencias
        return listaEquivalencias                                        #Retorna la lista completa después de procesar todas las líneas del archivo
    except FileNotFoundError:                                            #Captura el error si el nombre del archivo no existe en el directorio
        return "El archivo no se ha encontrado. Verifique que este bien escrito y con su formato, ejemplo: .txt"
