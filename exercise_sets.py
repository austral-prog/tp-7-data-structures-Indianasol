# Ejercicios de sets: catering del club de cocina

ALCOHOLS = {
    "whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch",
    "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco",
    "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur",
    "almond liqueur", "champagne", "orange curacao", "rum"
}


def clean_ingredients(nombre_plato, ingredientes):
    ing= set(ingredientes)
    return (nombre_plato, ing)
            


def check_drinks(nombre_bebida, ingredientes):
    for ingrediente in ingredientes:
        if ingrediente in ALCOHOLS:
            return nombre_bebida + " Cocktail"
    return nombre_bebida + " Mocktail"


def unique_chars(texto):
    letras = set()

    for letra in texto:
        letras.add(letra)
    return letras





    
def sum_set(numeros):
    suma = 0
    for numero in numeros:
        suma = suma + numero

    return suma


def common_elements(set_a, set_b):
    resultado= set()
    for elemento in set_a:
        if elemento in set_b:
            resultado.add(elemento)

    return resultado






    
