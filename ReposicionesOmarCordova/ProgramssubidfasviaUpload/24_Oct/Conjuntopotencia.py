def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def imprime_ordenado(c):
    """Imprime en la salida est�ndar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tama�o y
       luego lexicogr�ficamente. Cada subconjunto
       se imprime en su propia l�nea. Los
       elementos de los subconjuntos deben ser
       comparables entre s�, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)
imprime_ordenado(potencia(['cereza', 'chocolate', 'fresa', 'nuez', 'vainilla']))