
import random

print("------------------------------------")
print("---------- SUMA LISTA DATOS --------")
print("------------------------------------")

#Definicio de la funcion
def sumar_list_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

#Entrada
#  creamos una lista vacia
lista = [] 
# tamaño de la lista
n = int(input("Digite el tamaño de la lista: "))   

for i in range(n):
    num = random. randint(1,9)
    lista.append(num)

#Procesamiento
print("Lista: ", lista)
print("La suma es: ", sumar_lista_de_datos(lista))