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