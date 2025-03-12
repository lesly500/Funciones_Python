# usuario y que lo muestro numeros e veces en la pantalla digital. el valor de n es digital de el usuario

print("-------------------------------")
print("--MOSTRAR CADENA n VECES EN ---")
print("----------- PANTALLA-----------")
print("-------------------------------")
#Definicion de funcion
def mostrarCadena (cadena, n)
    for i in range(1,n+1)
        print(f"{i} . {cadena}")

#Entrada
cadena = input("igite la cadena a mostrar: ")        
n = int(input("Digite el numero de veces que quiere mostrar las cadena: "))

#procesamiento
mostrarCadena(cadena, n)

#salida
print("\nEso era....")