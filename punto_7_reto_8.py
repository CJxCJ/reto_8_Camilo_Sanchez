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
