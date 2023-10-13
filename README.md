# Reto 8 Camilo Sanchez

## Punto 1
1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.


````python
#se determina el rango del ciclo
for x in range(1, 101):
    #se define la funcion cuadrado
    cuadrado = x**2
    #se imprime el valor x y su respectivo cuadrado hasta que se acabe el ciclo
    print(x, cuadrado, sep=" , ")

````

## Punto 2
2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.


````python 
#simplemente se determina incio y fin de el ciclo y los valores que salta
for y in range(1, 1000, 2):
    #se imprime el listado
    print(y)
#se repite el mismo proceso cambiando los valores de inicio y final del ciclo
for x in range(2, 1001, 2):
    print(x)

````

## Punto 3
3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado


````python
#se pide que se ingrese un valor x
x = float(input("Ingrese un número: "))

#se determina incio y fin de el ciclo y los valores que resta
for i in range(int(x), 1, -1):
    #si la condicion de que el modulo de i entre 2 es 0 (es decir par) imprime el numero
    if i % 2 == 0:
        print(i)
    #de lo contrario sigue el ciclo hasta terminarlo
    else:
        continue

````

## Punto 4
4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
   

````python
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

````

## Punto 5
5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.


````python
#se pide que ingrese un numero entero x
x = int(input("ingrese un numero: "))
#se define la variable cuadrado para generar el conteo
cuadrado = 1
#el ciclo de i por el valor dado 
for i in range(x):
  #se multiplica por 2 la cantidad de veces que requiera el ciclo
  cuadrado *= 2
#imprime el resultado que seria 2 ^ al numero x
print(str(cuadrado))
````

## Punto 6
6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
   

````python
#se define la funcion potencia donde en el rango de y se multiplica la variable pot por x
def potencia(x:float, y:int):
    pot = 1.0
    for _ in range(y):
        pot *= x
    return pot
#se pide que ingrese un numero x real para la base de la potencia
x = float(input("ingrese un numero para la base: "))
#se pide que ingrese un numero y entero para el exponente de la potencia
y = int(input("ingrese otro numero para el exponente: "))
#el condicional decalra que si estos numeros son iguales o menores a 0 no se puede operar
if y < 0:
  print("los numeros deben ser reales mayores a 0")
#sino se opera los dos numeros
else:
  pot = potencia(x, y)
  print("El resultado de " + str(x)+ " elevado a la " + str(y) + " es " + str(pot))

````

## Punto 7
7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
   

````python
#se genera un ciclo del 1 al 9 (ya que el 10 no lo cuenta) para la tabla de multiplicar
for i in range(1, 10):
    #imprime el mensaje especificando que tabla es
    print("Tabla de multiplicar del: " + str(i))
    #se genera otro ciclo para los valores de la tabla de 1 al 10
    for j in range(1, 11):
        #se define que es la tabla
        tabla = i * j
        #se imprime la multiplicacion de el valor correnpondiente de i y j en ese momento y el resultado
        print(str(i) + " x " + str(j) + " = " + str(tabla))
    #se repite hasta que acabe el primer ciclo (i)    
    print()

````

## Punto 8
8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

````python
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



````

## Punto 9
9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

````python
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

````

## Punto 10
10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.


````python
import math

#función para calcular la aproximación de la función arcotangente
def aproxarctan(x, n):
    if abs(x) >= 1:
        raise ValueError("El valor de x debe estar en el rango [-1, 1].")
    
    aproximacion = 0

    for i in range(n):
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
        aproximacion += termino

    valor_real = math.atan(x)
    diferencia = abs(valor_real - aproximacion)
    
    return aproximacion, diferencia

#pedir que ingrese el valor de x en el rango [-1, 1] y el número de términos n.
x = float(input("Ingresa el valor de x en el rango [-1, 1]: "))
n = int(input("Ingresa el número de términos n: "))

#si x esté dentro del rango permitido [-1, 1].
if abs(x) > 1:
    print("El valor de x está fuera del rango permitido.")
else:
    #calcular la aproximación, la diferencia con el valor real e imprimir los resultados.
    aproximacion, diferencia = aproxarctan(x, n)
    print(f"Aproximación de arctan({x}) con {n} términos: {aproximacion}")
    print(f"Valor real de arctan({x}): {math.atan(x)}")
    print(f"Diferencia con el valor real: {diferencia:.4f}")

````

# Disclaimer: 
## fue lo mejor que logre, sinceramente fueron algo complicados incluso en la parte logica :,D
