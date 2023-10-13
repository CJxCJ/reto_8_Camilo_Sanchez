import math

#función para calcular la aproximación de la función seno 
def aprox_sen(x, n):
    aprox = 0

    for i in range(n):
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        aprox += termino

    valor = math.sin(x)
    dif = abs(valor - aprox)
    
    return aprox, dif

#función para obtener un error menor al 0.1%.
def error_aceptable(x, error_maximo=0.001):
    n = 0
    error = error_maximo + 1  
    while error > error_maximo:
        n += 1
        aproximacion, _ = aprox_sen(x, n)
        error = abs(math.sin(x) - aproximacion)
    return n

#se pide que ingrese el valor de x 
x = float(input("Ingresa el valor de x: "))
error_maximo = 0.001

#encontrar el valor de n necesario para cumplir con el error máximo.
n_max = error_aceptable(x, error_maximo)

#calcular la aproximación de sen(x) con n_max términos.
aprox, dif = aprox_sen(x, n_max)

#mostrar la respuesta
print(f"Para x = {x}, se necesita un mínimo de {n_max} para obtener menos del 0.1% de error.")
print(f"Aproximación de sen({x}) con {n_max} términos: {aprox}")
print(f"Diferencia con el valor real: {dif:.4f}")
