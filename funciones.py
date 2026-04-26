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

def mostrarTokens(listaEquivalencias):
    """
    función: Muestra en pantalla los tokens y sus equivalencias almacenados en la lista, formateados de manera clara.
    Entradas: listaEquivalencias(list): Lista que contiene las tuplas de tokens y sus equivalencias cargados en memoria.
    Salidas: Impresión en pantalla de los tokens y sus equivalencias en formato tabular. Si la lista está vacía, se muestra un mensaje indicando que no hay tokens cargados.
    """
    print("\n" + "=" * 50)                                               # Imprime una línea de separación para mejorar la legibilidad del formato
    print(f"{'TOKEN':<20} | {'EQUIVALENCIA'}")                           # Imprime los encabezados de las columnas con formato de alineación a la izquierda para el token y sin formato específico para la equivalencia
    print("-" * 50)
    if not listaEquivalencias:                                           # Verifica si la lista de equivalencias está vacía antes de intentar mostrar su contenido
        print("No hay tokens cargados en memoria.")                      # Si la lista está vacía, se muestra un mensaje informativo en lugar de intentar imprimir tokens inexistentes
    else:
        for tupla in listaEquivalencias:                                 # Recorre cada tupla en la lista de equivalencias para imprimir su contenido
            if isinstance(tupla, tuple) and len(tupla) > 1:              # Verifica formato y existencia de datos antes de imprimir
                print(f"{tupla[0]:<20} | {tupla[1]}")                    # Despliega equivalencia con formato de tabla
            else:
                if len(tupla) == 1:                                      # Si la tupla tiene solo un elemento, se asume que es un token sin equivalencia 
                    print(f"{tupla[0]:<20} | [Error: Sin equivalencia]") # Imprime el token con un mensaje de error indicando que no tiene una equivalencia definida.
    print("=" * 50 + "\n")                                               #Imprime el token y su significado en formato "token -> significado"
