# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):
    return registro[1]


def convert_coordinate(coordenada):
   return (coordenada[0], coordenada[1])
    

def create_record(registro_azara, registro_rui):
    tesoro = registro_azara[0]
    coordenada_azara = get_coordinate(registro_azara)
    
    
    ubicacion = registro_rui[0]
    cuadrante = registro_rui[2]
    coordenada_rui= registro_rui[1]
    
    coordenada_azara_convertida = convert_coordinate(coordenada_azara)

    if coordenada_azara_convertida == coordenada_rui:
        return (tesoro, coordenada_azara, ubicacion, coordenada_rui, cuadrante)
    else:
        return "not a match"
    

    

        


def sum_tuple(numeros):
    suma= 0
    if numeros == "":
        return 0
    for num in numeros:
        suma = suma + num
    return  suma


def count_occurrences(tupla, elemento):
    suma = 0

    for num in tupla:
        if num == elemento:
            suma = suma + 1
        else:
            suma = suma

    return suma


def find_index(tupla, elemento):
    suma = 0

    for num in tupla:
        if num == elemento:
            return suma

        suma = suma + 1
    return -1 


def filter_positives(numeros):
    tupla =()

    for num in numeros:
        if num > 0:
            tupla = tupla + (num,)

    return tupla
















    
