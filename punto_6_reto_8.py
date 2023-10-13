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
