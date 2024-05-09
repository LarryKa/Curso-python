# Escribir una tupla con los meses del año, luego, pide al usuario un numero, 
# el que haya ingresado, es el mes que debe mostrar en la tupla
tupla = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

numero = int(input("Ingresa un número correspondiente a un mes del año: "))

if len(tupla) >= numero and numero > 0:
    print(tupla[numero - 1])
else :
    print("debes elegir un número entre 1 y 12")
