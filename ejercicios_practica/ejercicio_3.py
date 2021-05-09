# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo

# Almacenar su nombre completo en una variable
# nombre_completo = .....

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)

nombre_completo = nombre + ' ' + apellido
print('mi nombre completo es', nombre_completo)

nombre_sin_espacios = nombre + apellido 'nueva variable sin espacios para que no tome el "espacio" como un caracter adicional'

cantidad_letras = len(nombre_sin_espacios)
print('mi nombre completo tiene', cantidad_letras, 'caracteres')