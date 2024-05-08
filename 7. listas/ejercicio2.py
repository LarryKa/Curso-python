"""
Escribe una lista que tenga los números de 1 al 10. 
Luego, debes hacer que los datos que están en las posiciones: 
4, 7 y 9 sean multiplicados por 2; 
por último, mostrar la lista nueva con los nuevos datos
"""

lista = []
i = 1
while(i <= 10): 
    lista.append(i)
    i += 1

lista[3] *= 2
lista[6] *= 2
lista[8] *= 2
print(lista)