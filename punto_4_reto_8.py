# se define la variable factorial para generar un conteo
factorial = 1
#se pide que se ingrese un numero entero x
x = int(input("Introduzca el número: "))
#se determina un ciclo de 1 a x + 1
for i in range(1, x + 1):
    #se muntiplica la variable factorial por el valor de la lista
    factorial *= i
#se imprime el resultado de la variable factorial para cuando acabe el ciclo
print("El factorial de " + str(x) + " es " + str(factorial))
