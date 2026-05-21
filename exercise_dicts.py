# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
    
    dicc = {}
    for item in items:
        if item in dicc:
            dicc[item] = dicc[item] +1
        else:
            dicc[item]= 1
    return dicc
def add_items(inventario, items):

    for item in items:

        if item in inventario:
            inventario[item] = inventario[item] + 1
        else:
            inventario[item] = 1

    return inventario


def decrement_items(inventario, items):
    for item in items:
        if item in inventario:
            if inventario[item] > 0:
                inventario[item] = inventario[item] - 1

    return inventario

def remove_item(inventario, item):
    if item in inventario:
        del inventario[item]

    return inventario




def list_inventory(inventario):
    resultado = []

    for item, cantidad in inventario.items():
        if cantidad > 0:
            resultado.append((item, cantidad))

    return resultado




def find_max_value(diccionario):
    if diccionario == {}:
        return ""

    mayor_nombre = ""
    mayor_puntaje = None

    for nombre, puntaje in diccionario.items():
        if mayor_puntaje == None or puntaje > mayor_puntaje:
            mayor_puntaje = puntaje
            mayor_nombre = nombre

    return mayor_nombre


def reverse_dict(diccionario):
    resultado = {}

    for clave, valor in diccionario.items():
        if valor in resultado:
            resultado[valor] = resultado[valor] + clave
        else:
            resultado[valor] = clave

    return resultado




def word_frequency(palabras):
    if palabras == "":
        return {}

    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] = frecuencia[palabra] + 1
        else:
            frecuencia[palabra] = 1

    return frecuencia


def find_biggest_expense(gastos):
    if gastos == {}:
        return ""

    categoria_mayor = ""
    promedio_mayor = None

    for categoria, lista_gastos in gastos.items():
        suma = 0

        for gasto in lista_gastos:
            suma = suma + gasto

        promedio = suma / len(lista_gastos)

        if promedio_mayor == None or promedio > promedio_mayor:
            promedio_mayor = promedio
            categoria_mayor = categoria

    return categoria_mayor

def sum_expenses(gastos):
    resultado = {}

    for categoria, lista_gastos in gastos.items():
        suma = 0

        for gasto in lista_gastos:
            suma = suma + gasto

        resultado[categoria] = suma

    return resultado

def sum_expenses_by_type(gastos):
    resultado = {}

    for categoria, lista_tuplas in gastos.items():
        for tipo, monto in lista_tuplas:
            if tipo in resultado:
                resultado[tipo] = resultado[tipo] + monto
            else:
                resultado[tipo] = monto

    return resultado










    
    
