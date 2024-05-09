# En el siguiente diccionario se encuentran capitales de los paises en el mundo, 
# debes realizar un programa que pida un pais al usuario, 
# y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, 
# se debe mostrar un mensaje diciendo que ese pais no se encuentra.

paises = {
    "Guatemala": "Ciudad de Guatemala", 
    "El Salvador": "San Salvador", 
    "Honduras": "Honduras","Nicaragua": "Managua", 
    "Costa Rica": "San Jose", 
    "Panama": "Panama", 
    "Argentina": "Buenos Aires", 
    "Colombia": "Bogota", 
    "Venezuela": "Caracas", 
    "España": "Madrid"
}

paisSeleccionado = input("Escribe el nombre de un pais: ")

if paisSeleccionado.title() in paises :
    print('La capital de {} es {}'.format( paisSeleccionado, paises[paisSeleccionado.title()]) )
else:
    print('El pais no se encuentra')

