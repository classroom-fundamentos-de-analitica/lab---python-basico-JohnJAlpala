"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = "data.csv"
    cantidad = 0
    with open(data,"r") as data:
        #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            cantidad += int(lista[1])
    data.close()

    return cantidad


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = "data.csv"
    counts = {}
    with open(data,"r") as data:
        #next(data, None)
        for linea in data:
            letter = linea[0]
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    result = sorted(list(counts.items()), key=lambda x: x[0])
    data.close()
    return result


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = "data.csv"
    suma_letras = {}
    with open(data,"r") as data:
        #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            letra = lista[0]
            valor = int(lista[1])
            if letra in suma_letras:
                suma_letras[letra] += valor
            else:
                suma_letras[letra] = valor

    # Crear una lista de tuplas a partir del diccionario ordenando alfabéticamente las claves
    resultado = sorted([(letra, suma_letras[letra]) for letra in suma_letras])
    data.close()
    return resultado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = "data.csv"
    counts = {}
    with open(data,"r") as data:
        #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            letter = lista[2][5:7]

            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    result = sorted(list(counts.items()), key=lambda x: x[0])
    data.close()
    return result


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = "data.csv"
    diccionario = {}
    with open(data,"r") as data:
        #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            letra = lista[0]
            valor = lista[1]
            if letra not in diccionario:
              diccionario[letra] = []
              diccionario[letra].append(valor)
            else:
              diccionario[letra].append(valor)
            # Encontrar los valores máximos y mínimos para cada letra
    data.close()
    result = []
    for letra, valores in diccionario.items():
        maximo = max(valores)
        minimo = min(valores)
        result.append((letra, maximo, minimo))
        result.sort()
    
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = "data.csv"
    diccionario = {}
    with open(data,"r") as data:
        #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            columna5 = lista[4]
            elementos = columna5.split(",")
            for elemento in elementos:
              clave, valor = elemento.split(":")
              if clave not in diccionario:
                  diccionario[clave] = []
              diccionario[clave].append(int(valor))
        # Encontrar los valores máximos y mínimos para cada letra
        result = []
        for clave, valores in diccionario.items():
            minimo = min(valores)
            maximo = max(valores)
            result.append((clave, minimo, maximo))
            result.sort()
    data.close()
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = "data.csv"
    valores_letras = {}
    with open(data,"r") as data:
        #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            valor = int(lista[1])
            letra = lista[0]
            
            if valor not in valores_letras:
                # Si el valor no está en el diccionario, lo agregamos con una lista vacía
                valores_letras[valor] = []
            
            # Agregamos la letra a la lista asociada al valor
            valores_letras[valor].append(letra)
    
    # Convertimos el diccionario en una lista de tuplas y la ordenamos por el valor de la columna 2
    lista_tuplas = sorted([(valor, letras) for valor, letras in valores_letras.items()])
    data.close()
    return lista_tuplas


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = "data.csv"
    letras_por_valor = {}
    with open(data,"r") as data:
        #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            valor_columna_2 = int(lista[1])
            letra_columna_1 = lista[0]
            
            if valor_columna_2 not in letras_por_valor:
              letras_por_valor[valor_columna_2] = []
        
            if letra_columna_1 not in letras_por_valor[valor_columna_2]:
                letras_por_valor[valor_columna_2].append(letra_columna_1)

    # ordenamos alfabéticamente las listas de letras asociadas a cada valor de la segunda columna
        for valor in letras_por_valor:
            letras_por_valor[valor].sort()
            
    # creamos la lista de tuplas a partir del diccionario
        lista_tuplas = [(valor, letras_por_valor[valor]) for valor in sorted(letras_por_valor)]
    data.close()
    return lista_tuplas


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = "data.csv"
    counts = {}
    with open(data,"r") as data:
        #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            columna5 = lista[4]
            elementos = columna5.split(",")
            for elemento in elementos:
              clave = elemento[:3]
              if clave in counts:
                counts[clave] += 1
              else:
                  counts[clave] = 1
        counts = dict(sorted(counts.items(), key=lambda x: x[0]))
    data.close()
    return counts


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = "data.csv"
    resultados  = []
    with open(data,"r") as data:
    #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            letra_columna_1 = lista[0]
            cantidad_columna_4 = len(lista[3].split(','))
            cantidad_columna_5 = len(lista[4].split(','))
            #print(columna5)
            tupla_resultado = (letra_columna_1, cantidad_columna_4, cantidad_columna_5)
            resultados.append(tupla_resultado)
    data.close()      
    return resultados


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = "data.csv"
    counts = {}
    with open(data,"r") as data:
        #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            columna4 = lista[3]
            columna2 = int(lista[1])
            elementos = columna4.split(",")
            for elemento in elementos:
              clave = elemento[:3]
              if clave in counts:
                counts[clave] += columna2
              else:
                counts[clave] = columna2

    resultado = {letra: counts[letra] for letra in sorted(counts)}
    data.close()
    return resultado


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = "data.csv"
    diccionario = {}
    with open(data,"r") as data:
    #next(data, None)
        for linea in data:
            linea = linea.rstrip()
            separador = "\t"
            lista = linea.split(separador)
            clave_columna_1 = lista[0]
            columna5 = lista[4]
            elementos = columna5.split(",")
            #print(columna5)
            for elemento in elementos:
                valor_columna_5 = int(elemento.split(':')[1])
                if clave_columna_1 in diccionario:
                    diccionario[clave_columna_1] += valor_columna_5
                else:
                    diccionario[clave_columna_1] = valor_columna_5

    resultado = {letra: diccionario[letra] for letra in sorted(diccionario)}
    data.close()
    return resultado
            
