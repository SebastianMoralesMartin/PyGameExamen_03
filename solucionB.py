# Encoding: UTF-8
# Sebastian Morales Martin
# solucionB.py: Examen de segund registro

def recorrerDerecha(lista):
    valor = lista.count(lista)

    reemplazo = lista.pop(valor -1)
    lista.insert(0, reemplazo)

    return lista

def calcularReprobados(lista):
    contador = 0
    totalPosible = len(lista)
    for numero in lista:
        if numero < 70:
            contador +=1
    porcentaje = (contador/totalPosible)*100
    return porcentaje

def contarMenores(lista, n):
    menorOIgual = 0
    for numero in lista:
        if numero <= n:
            menorOIgual += 1
    return menorOIgual


