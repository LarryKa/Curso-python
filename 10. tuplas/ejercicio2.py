# Escribir una tupla que tenga las letras del alfabeto. 
# Luego, debes pedir al usuario un número, el que haya ingresado, 
# es la letra que debe imprimir el programa

alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

numero = int(input("Escribe un número del 1 al 27: "))

if len(alfabeto) >= numero and numero > 0 :
    print( alfabeto[numero-1] )
else :
    print( "no elegiste un número entre 1 y 27")