#Programa Principal / Menu tarea principal
# Elaborado por: Gabriel Josue Marin Munoz y Derian Segura
# Fecha de elaboración: 25/04/2026 10:10 am
# fecha de última actualización: 26/04/2026 11:38am
#version de python: 3.14.3

#importaciones
import re

#funciones
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
        tokensActualizados = ""                                          #Se unicializa vacia estrategicamente para almacenar los tokens actualizados
        for linea in archivo:                                            #Inicia un ciclo para procesar cada una de las líneas del documento
            linea = linea.strip()                                        #Se elimina el salto de linea al final del texto para limpiar el dato
            linea = re.sub(rf"\s*{metodoSeparacion}\s*", metodoSeparacion, linea) #Dentro de la linea, antes y despues del metodo de separacion, dejara el texto sin espacios 
            linea = linea.split(metodoSeparacion)                        #Divide la hilera en partes según el separador indicado por el usuario
            linea = tuple(linea)                                         #Convierte el par de datos en una tupla para cumplir con el formato de almacenamiento
            encontrado = False                                           #Bandera que ayuda a determinar si el token es nuevo o una reescritura
            for tupla in range(len(listaEquivalencias)):                 #Ciclo que recorre los índices de la lista para buscar coincidencias
                if linea[0] == listaEquivalencias[tupla][0]:       
                    tokensActualizados += linea[0] + ", "
                    listaEquivalencias[tupla] = linea                    #Reemplaza la tupla vieja por la nueva en la posición exacta encontrada
                    encontrado = True                                    #Marca como encontrado para no agregar el token como si fuera nuevo
                    break                                                #Sale del ciclo de búsqueda al haber logrado el reemplazo
            if not encontrado:                                           
                listaEquivalencias.append(linea)                         #Agrega la nueva tupla al final de la lista de equivalencias
        if len(tokensActualizados) != 0:
            print(f"Se reescribió {tokensActualizados[:-2]}, y conservaran el reemplazo más reciente.") #Notifica al usuario sobre la sustitución del valor
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
def agregarModificarTokens(nuevosTokens, nuevoSeparador, listaEquivalencias):       #str=texto + int=entero + print=imprima
    tokensActualizados = ""
    TokensDivididos = nuevosTokens.split("+")
    for token in TokensDivididos:
        partesToken = token.split(nuevoSeparador)
        tokenLimpio = partesToken[0]
        tokenLimpio = tokenLimpio.strip()
        equivalenciaLimpia = partesToken[1]
        equivalenciaLimpia = equivalenciaLimpia.strip()
        nuevaTupla = (tokenLimpio, equivalenciaLimpia)
        encontrado = False
        for tupla in range(len(listaEquivalencias)):
            if listaEquivalencias[tupla][0] == tokenLimpio:
                tokensActualizados += nuevaTupla[0] + ", "
                listaEquivalencias[tupla] = nuevaTupla
                encontrado = True
                break
        if not encontrado:                                           
            listaEquivalencias.append(nuevaTupla)
    if len(tokensActualizados) != 0:
        print(f"Se reescribió {tokensActualizados[:-2]}, y conservaran el reemplazo más reciente.")
    return listaEquivalencias
def guardarTokens(nombreArchivoGuardar, metodoSeparacion, listaEquivalencias):   
    """
    Función: Guarda la lista de tokens y sus equivalencias en un archivo de texto, utilizando el método de separación indicado por el usuario.
    Entradas:
    -nombreArchivoGuardar(str): Nombre del archivo físico donde se desea guardar los tokens y sus equivalencias.
    -metodoSeparacion(str): Carácter separador que divide el token de su significado, ejemplo: "->", "=", ",".
    -listaEquivalencias(list): Lista que contiene las tuplas de tokens y sus equivalencias que se desean guardar.
    Salidas:
    -Archivo de texto: Se crea o sobrescribe un archivo con el nombre especificado, conteniendo los tokens y sus equivalencias formateados según el método de separación elegido. Si la lista está vacía, se guarda un mensaje indicando que no hay tokens para guardar.
    """
    if len(listaEquivalencias) == 0:                                     #Verifica si la lista de equivalencias está vacía antes de intentar guardar su contenido
            return "Error: No hay tokens en memoria para guardar. Cargue o agregue algunos primero." # Si la lista está vacía, se retorna un mensaje de error
    try: 
            archivoGuardar = open(nombreArchivoGuardar, "w")             #Se abre el archivo en modo escritura "w" para guardar los datos, si el archivo no existe se crea uno nuevo
            contadorTokens = 0
            for tupla in listaEquivalencias:                             #Recorre cada tupla en la lista de equivalencias para escribir su contenido en el archivo
                if len(tupla) == 2:                                      #Verifica que la tupla tenga exactamente dos elementos (token y equivalencia) 
                    linea = tupla[0] + metodoSeparacion + tupla[1] + "\n" #Formatea la línea a escribir en el archivo utilizando el método de separación elegido por el usuario y añadiendo un salto de línea al final
                    archivoGuardar.write(linea)                          #Escribe la línea formateada en el archivo
                    contadorTokens += 1                                  #Cuenta cuantos tokens se guardan
                else:
                    print("Aviso: Se saltó un dato incompleto en la lista.")
            archivoGuardar.close()                                       #Cierra el archivo despues de escribir los tokens
            return f"Se guardaron {contadorTokens} tokens en el archivo '{nombreArchivoGuardar}'" 
    except:                                                              #Captura cualquier error que pueda ocurrir durante el proceso de escritura del archivo
            return "No se pudo escribir en el archivo. \n Verifique que el nombre sea válido o que coincida con el formato:ejemplo: .txt" # Si ocurre un error, retorna el mensaje de error con retroalimentacion. 