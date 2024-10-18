from agregar import agregar_libro
from mostrar import mostrar_libro
from comparar import comparar_paginas
from buscar import buscar_por_autor
from paginas_totales import calcular_paginas_totales
from libro_mas_largo import libro_mas_largo
from formato import formato_libros

libro1 = agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
libro2 = agregar_libro("Don Quijote", "Miguel de Cervantes", 863)
libro3 = agregar_libro("El Principito", "Antoine de Saint-Exupéry", 96)

lista_libros = [libro1, libro2, libro3]

print("Información del libro 1:")
print(mostrar_libro(libro1))

print("\nComparar el número de páginas entre libro1 y libro2:")
print(f"El libro con más páginas es: {comparar_paginas(libro1, libro2)}")

print("\nBuscar libros por autor 'Gabriel García Márquez':")
print(buscar_por_autor(lista_libros, "Gabriel García Márquez"))

print("\nTotal de páginas de todos los libros:")
print(calcular_paginas_totales(lista_libros))

print("\nEl libro más extenso es:")
libro_extenso = libro_mas_largo(lista_libros)
print(mostrar_libro(libro_extenso))

print("\nFormato de todos los libros:")
for libro_formato in formato_libros(lista_libros):
    print(libro_formato)