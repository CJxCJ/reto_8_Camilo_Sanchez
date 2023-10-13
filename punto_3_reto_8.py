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
