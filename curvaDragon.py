num = int(input("Ingresa el numero; "))
def cuenta(n):
    lista = []
    if n == 0:
        return lista
    else:
        p = cuenta(n - 1)
        r = p[::-1]
        i = ['L' if g == 'R' else 'R' for g in r]
        return p + ['L'] + i
print (cuenta(num))
