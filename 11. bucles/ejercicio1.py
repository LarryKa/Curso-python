# Escribir un programa que pida un numero al usuario 
# y muestre las tablas de multiplicar de ese numero
i = 0
numero = int(input("Ingresa un número: "))

while i < 10 :
    i += 1
    print("numero X {} = {}".format(i, i * numero))