

import ramdon

print("-------------------------------------")
print("----- PROMEDIO LISTA DATOS ----------")
prin("--------------------------------------")

#Definicion de la funcion
def calcular_promedio_lista(lista):
    suma = 0
    for i in lista:
        suma = suma + 1
    promedio = suma / len(lista)
    return promedio

#Entrada
# Creamos una lista vacia
lista = []
# Tamaño de la lista
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = ramdon.randint(14,18)
    lista.append(num)

#Procesamiento
prin("lista: ", lista)
print("El promedio de la lista es: ", calcular_promedio_lista(lista))

#salida
print("\nEso era...")