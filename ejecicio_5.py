# construir una funcion que reciba como parametro una lista de datos numericos y retorne el promedio de los daots pares.
import random
def suma_y_promedio_pares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    if len(pares) == 0:
        return "No hay números pares en la lista"
    suma = sum(pares)
    promedio = suma / len(pares)
    return suma, promedio

n = int(input("Digite el tamaño de la lista: "))
lista_numeros = [random.randint(1, 9) for _ in range(n)]

print("Los números generados son:", lista_numeros)

suma, promedio = suma_y_promedio_pares(lista_numeros)

if suma == "No hay números pares en la lista":
    print(suma)
else:
    print("La suma de los números pares es:", suma)
    print("El promedio de los números pares es:", promedio)