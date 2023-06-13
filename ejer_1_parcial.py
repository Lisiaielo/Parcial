def contar_palabra(vector, palabra):
    # Caso base: el vector está vacío
    if len(vector) == 0:
        return 0

    # Caso recursivo: contar la palabra en el primer elemento del vector
    # y llamar a la función recursivamente con el resto del vector
    if vector[0] == palabra:
        return 1 + contar_palabra(vector[1:], palabra)
    else:
        return contar_palabra(vector[1:], palabra)

vector_palabras = ["Hola", "mundo", "Hola", "hola", "adiós", "Hola"]
palabra_a_contar = "Hola"
resultado = contar_palabra(vector_palabras, palabra_a_contar)
print(f"La palabra '{palabra_a_contar}' aparece {resultado} veces.")
