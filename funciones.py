#Programa Principal / Menu tarea principal
# Elaborado por: Gabriel Josue Marin Munoz y Derian Segura
# Fecha de elaboración: 25/04/2026 10:10 am
# fecha de última actualización: 01/05/2026 5:37
#version de python: 3.14.3

#importaciones
import re
import csv

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
        archivo = open(nombreArchivoTokens, "r")
        print("\nleyendo el archivo...\n")
        tokensActualizados = ""
        for linea in archivo:
            linea = linea.strip()
            partesToken = linea.split(metodoSeparacion)
            tokenLimpio = partesToken[0]
            tokenLimpio = tokenLimpio.strip()
            equivalenciaLimpia = partesToken[1]
            equivalenciaLimpia = equivalenciaLimpia.strip()
            nuevaTupla = (tokenLimpio, equivalenciaLimpia)
            encontrado = False
            for tupla in range(len(listaEquivalencias)):
                if nuevaTupla[0] == listaEquivalencias[tupla][0]:
                    tokensActualizados += nuevaTupla[0] + ", "
                    listaEquivalencias[tupla] = nuevaTupla
                    encontrado = True
                    break
            if encontrado == False:
                listaEquivalencias.append(nuevaTupla)
        archivo.close
        if len(tokensActualizados) != 0:
            print(f"Se reescribió {tokensActualizados[:-2]}, y conservaran el reemplazo más reciente.")
        return listaEquivalencias
    except FileNotFoundError:
        return "El archivo no se ha encontrado. Verifique que este bien escrito y con su formato, ejemplo: .txt"
    
def mostrarTokens(listaEquivalencias):
    """
    función: Muestra en pantalla los tokens y sus equivalencias almacenados en la lista, formateados de manera clara.
    Entradas: listaEquivalencias(list): Lista que contiene las tuplas de tokens y sus equivalencias cargados en memoria.
    Salidas: Impresión en pantalla de los tokens y sus equivalencias en formato tabular. Si la lista está vacía, 
    se muestra un mensaje indicando que no hay tokens cargados.
    """
    print("\n" + "=" * 50)
    print(f"{'TOKEN':<20} | {'EQUIVALENCIA'}")
    print("-" * 50)
    if not listaEquivalencias:
        print("No hay tokens cargados en memoria.")
    else:
        for tupla in listaEquivalencias:
            if isinstance(tupla, tuple) and len(tupla) > 1:
                print(f"{tupla[0]:<20} | {tupla[1]}")
            else:
                if len(tupla) == 1:
                    print(f"{tupla[0]:<20} | [Error: Sin equivalencia]")
    print("=" * 50 + "\n")
def agregarModificarTokens(nuevosTokens, nuevoSeparador, listaEquivalencias):
    """
    funcion: Permite al usuario agregar tokens que no esten dentro de los archivos o darle al usuario la opcicion
    de modificar o actualizar los tokens que ya hayan sido encontrados en los archivos 
    Entradas:
    nuevosToken(str): Es una cadena de texto la cual contiene los tokens, su separador y su equivalencia siendo 
    por un signo de +
    nuevoSeparador(str): simbolo que sera utilizado para separar los tokens de su equivalencia para ser almacenados
    en una lista de tuplas
    listaEquivalencias(lista): lista que contiene las tuplas de token y equivalencia, utilizada para buscar dentro
    de ella los tokens identicos para modificarlos o agregar los que todavia no existen
    Salidas:
    listaEquivalencias(lista): lista que contiene las tuplas de los tokens y equivalencias de manera actualizada
    """
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
                print(f"\n{nuevaTupla} ya esta registrada como {listaEquivalencias[tupla]}...\n deseas actualizar {listaEquivalencias[tupla]} por {nuevaTupla}?")
                desicion = input("\nOpciones: \n1 - Si\n2 - No\n\n Digite su respuesta: ")
                if desicion == "1":
                    tokensActualizados += nuevaTupla[0] + ", "
                    listaEquivalencias[tupla] = nuevaTupla
                    encontrado = True
                    break
                elif desicion == "2":
                    encontrado = True
                    break
                else:
                    print("Su opcion no es valida, debe ser 1 o 2 unicamente.")
        if encontrado == False:                                           
            listaEquivalencias.append(nuevaTupla)
    if len(tokensActualizados) != 0:
        print(f"\nSe reescribió {tokensActualizados[:-2]}, y conservaran el reemplazo más reciente.")
    return listaEquivalencias
def guardarTokens(nombreArchivoGuardar, metodoSeparacion, listaEquivalencias):   
    """
    Función: Guarda la lista de tokens y sus equivalencias en un archivo de texto, utilizando el método de
    separación indicado por el usuario.
    Entradas:
    -nombreArchivoGuardar(str): Nombre del archivo físico donde se desea guardar los tokens y sus equivalencias.
    -metodoSeparacion(str): Carácter separador que divide el token de su significado, ejemplo: "->", "=", ",".
    -listaEquivalencias(list): Lista que contiene las tuplas de tokens y sus equivalencias que se desean guardar.
    Salidas:
    -Archivo de texto: Se crea o sobrescribe un archivo con el nombre especificado, conteniendo los tokens y 
    sus equivalencias formateados según el método de separación elegido. Si la lista está vacía, se guarda un 
    mensaje indicando que no hay tokens para guardar.
    """
    if len(listaEquivalencias) == 0:
            return "Error: No hay tokens en memoria para guardar. Cargue o agregue algunos primero."
    try: 
            archivoGuardar = open(nombreArchivoGuardar, "w")
            contadorTokens = 0
            for tupla in listaEquivalencias:
                if len(tupla) == 2: 
                    linea = tupla[0] + metodoSeparacion + tupla[1] + "\n" 
                    archivoGuardar.write(linea)
                    contadorTokens += 1
                else:
                    print("Aviso: Se saltó un dato incompleto en la lista.")
            archivoGuardar.close()
            return f"Se guardaron {contadorTokens} tokens en el archivo '{nombreArchivoGuardar}'" 
    except:
            return "No se pudo escribir en el archivo. \n Verifique que el nombre sea válido o que coincida con el formato:ejemplo: .txt"
            
def separarPalabraParensis(linea):
    """
    Funcionamiento: Agrega espacios alrededor de los paréntesis en una línea de texto. Esto permite que el programa 
    reconozca los paréntesis y las palabras como elementos separados (tokens) en lugar de un solo bloque.
    Entradas:
    linea (str): Una cadena de texto que representa una línea de código leída desde el archivo.
    Salida:
    texto (str): La cadena original procesada, donde cada paréntesis ha sido rodeado por espacios (ej. ( se convierte en ().
    """
    texto = ""
    for caracter in linea:
        if caracter == "(":
            texto += " ( "
        elif caracter == ")":
            texto += " ) "
        else:
            texto += caracter
    return texto

def traducirCodigo(nombreArchivo, listaEquivalencias):
    """
    Funcionamiemto: Lee un archivo de texto palabra por palabra y reemplaza los términos encontrados en la lista de
    equivalencias por su traducción. Mantiene las palabras originales si no tienen traducción y gestiona errores de lectura o archivos vacíos.
    Entradas:
    nombreArchivo (str): Nombre del archivo a traducir.
    listaEquivalencias (list): Lista de tuplas con los pares (original, traducción).
    Salidas:
    resultado (str): El texto traducido o un mensaje de error según el caso.
    """
    try:
        coincidenciaEquivalencia = False
        resultado = ""
        archivoATraducir = open(nombreArchivo, "r")
        print("\nLeyendo archivo...\n")
        contenido = archivoATraducir.read()
        if not contenido:
            return "El archivo que introdujo esta vacio\n"
        archivoATraducir.seek(0)
        for linea in archivoATraducir:
            if "(" in linea or ")" in linea:
                    linea = separarPalabraParensis(linea)
            linea = linea.split(" ")
            for palabra in linea:
                if palabra != "":
                    TokenEncontrado = False
                    for tupla in listaEquivalencias:
                        if palabra == tupla[0]:
                            resultado += tupla[1] + " "
                            TokenEncontrado = True
                            coincidenciaEquivalencia = True
                            break
                    if TokenEncontrado == False:
                        resultado += palabra + " "
                else:
                    resultado += " "
        if coincidenciaEquivalencia == False:
            return "\nNo se encontraron palabras que coincidan con los Tokens, recuerde cargarlos y verificar que esten escritos identicamente\n"
        return resultado
    except FileNotFoundError:
        return "\nArchivo no encontrado, verifica que este bien escrito junto con su formato, como en el siguiente ejemplo: archivo.txt\n"

def generarReporteCvs(nombreReporte, textoATraducir, listaEquivalencias):
    '''
    funcionamiento: crea un recuento de cuantas veces aparece cada palabra original en el texto traducido
    '''
    if not listaEquivalencias:
        return ' No hay tokens para el reporte'
    try: 
        if not nombreReporte.lower().endswith(".csv"):
            nombreReporte += ".csv"
        archivo = open(nombreReporte, "w", newline="", encoding="utf-8")
        escritor= csv.writer(archivo)
        escritor.writerow(["palabra", "token", "cantidad"])
        for tupla in listaEquivalencias:
            token = tupla[0]
            palabra = tupla[1]
            conteo = textoATraducir.lower().count(palabra.lower())
            escritor.writerow([palabra, token, conteo])  
        archivo.close()
        return f"Reporte '{nombreReporte}' generado con éxito."
    except Exception as e:
        return f'Error al generar el reporte: {str(e)}'
