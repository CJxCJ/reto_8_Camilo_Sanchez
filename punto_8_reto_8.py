import math

#definimos una funcion para la aproximacion 
def aprox_exp(x, y):
    aprox = 0
    valor = math.exp(x)
    #definimos el 0.1% de error
    error = 0.001  

    
    #operamos x elevado al valor del rango divido el factorial de de este mismo
    for i in range(y):
        termino = (x ** i) / math.factorial(i)
        aprox += termino
        #si el valor absoluto del termino es menor al 0.1% de error 
        if abs(termino) < error:
            #devuelve la aproximación y el valor de y
            return aprox, i + 1  

    return aprox, y

#pide que se ingrese un numero x
x = float(input("Ingrese el valor de x: "))

y = 1
#el sciclo se define que mientras sea cierto
while True:
    #llamamos la funcion
    aprox, y_aprox = aprox_exp(x, y)
    #si el valor de aprox no coincide con ninguno rompe el ciclo 
    if aprox is not None:
        break
    y += 1

print("Aproximación de e ^"  + str(x) + ": " + str(aprox))
print("Valor real de e ^" + str(x) + ": " + str(math.exp(x)))
print(f"Diferencia entre la aproximación y el valor real: {abs(aprox - math.exp(x))}")
print("Valor de n con menos del 0.1% de error: " + str(y_aprox))


