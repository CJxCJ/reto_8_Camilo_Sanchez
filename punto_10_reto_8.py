import math

# Función para calcular la aproximación de la función arcotangente usando los primeros n términos de la serie de Maclaurin.
def aproximacion_arcotangente(x, n):
    if abs(x) >= 1:
        raise ValueError("El valor de x debe estar en el rango [-1, 1].")
    
    aproximacion = 0

    for i in range(n):
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
        aproximacion += termino

    valor_real = math.atan(x)
    diferencia = abs(valor_real - aproximacion)
    
    return aproximacion, diferencia

# Solicitar al usuario que ingrese el valor de x en el rango [-1, 1] y el número de términos n.
x = float(input("Ingresa el valor de x en el rango [-1, 1]: "))
n = int(input("Ingresa el número de términos n: "))

# Verificar que el valor de x esté dentro del rango permitido [-1, 1].
if abs(x) > 1:
    print("El valor de x está fuera del rango permitido.")
else:
    # Calcular la aproximación y la diferencia con el valor real.
    aproximacion, diferencia = aproximacion_arcotangente(x, n)
    print(f"Aproximación de arctan({x}) con {n} términos: {aproximacion}")
    print(f"Valor real de arctan({x}): {math.atan(x)}")
    print(f"Diferencia con el valor real: {diferencia:.4f}")
