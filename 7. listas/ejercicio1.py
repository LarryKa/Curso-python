"""
En la siguiente lista, debes hacer un programa que muestre los valores al usuario, 
a su vez, 
debe pedir dos datos y esos que sean ingresados deben ser sustituidos 
en el primer y segundo lugar:
"""
lista = [20, 50, "Curso", 'Python', 3.14]

dato1 = input("ingresa el primer dato: ")
dato2 = input("ingresa el segundo dato: ")

lista[0] = dato1
lista[1] = dato2

print(lista)

