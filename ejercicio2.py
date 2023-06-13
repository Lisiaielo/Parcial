from queue import Queue

# Definir la lista de superhéroes
avengers = [
    {'nombre_superheroe': 'Star Lord', 'nombre_personaje': 'Peter Quill', 'grupo': 'Guardianes de la galaxia', 'anio_aparicion': 1976},
    {'nombre_superheroe': 'Capitana Marvel', 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': 2012},
    {'nombre_superheroe': 'Iron Man', 'nombre_personaje': 'Tony Stark', 'grupo': '', 'anio_aparicion': 1963},
    {'nombre_superheroe': 'Black Widow', 'nombre_personaje': 'Natasha Romanoff', 'grupo': '', 'anio_aparicion': 1964},
    {'nombre_superheroe': 'Captain America', 'nombre_personaje': 'Steve Rogers', 'grupo': '', 'anio_aparicion': 1941},
    {'nombre_superheroe': 'Thor', 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': 1962},
    {'nombre_superheroe': 'Hulk', 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': 1962},
    {'nombre_superheroe': 'Hawkeye', 'nombre_personaje': 'Clint Barton', 'grupo': '', 'anio_aparicion': 1964},
    {'nombre_superheroe': 'Black Panther', 'nombre_personaje': 'T\'Challa', 'grupo': '', 'anio_aparicion': 1966},
    {'nombre_superheroe': 'Scarlet Witch', 'nombre_personaje': 'Wanda Maximoff', 'grupo': '', 'anio_aparicion': 1964}
]

# a. Determinar si "Capitana Marvel" está en la lista y mostrar su nombre de personaje
capitana_marvel = next((hero['nombre_personaje'] for hero in avengers if hero['nombre_superheroe'] == 'Capitana Marvel'), None)
if capitana_marvel:
    print(f"El nombre de personaje de Capitana Marvel es: {capitana_marvel}")
else:
    print("Capitana Marvel no está en la lista.")

# b. Almacenar los superhéroes que pertenezcan al grupo "Guardianes de la galaxia" en una cola e indicar cuántos son
guardians_queue = Queue()
guardians_count = 0
for hero in avengers:
    if hero['grupo'] == 'Guardianes de la galaxia':
        guardians_queue.put(hero)
        guardians_count += 1
print(f"La cantidad de superhéroes que pertenecen al grupo 'Guardianes de la galaxia' es: {guardians_count}")

# c. Mostrar de manera descendente los superhéroes que pertenecen a los grupos "Los cuatro fantásticos" y "Guardianes de la galaxia"
fantastic_four_and_guardians = sorted([hero['nombre_superheroe'] for hero in avengers if hero['grupo'] in ['Los cuatro fantásticos', 'Guardianes de la galaxia']], reverse=True)
print("Superhéroes de 'Los cuatro fantásticos' y 'Guardianes de la galaxia' en orden descendente:")
for hero in fantastic_four_and_guardians:
    print(hero)

# d. Listar los superhéroes que tengan nombre de personaje cuyo año de aparición sea posterior a 1960
heroes_after_1960 = [hero['nombre_superheroe'] for hero in avengers if hero['nombre_personaje'] != '' and hero['anio_aparicion'] > 1960]
print("Superhéroes con nombre de personaje cuyo año de aparición es posterior a 1960:")
for hero in heroes_after_1960:
    print(hero)

# e. Corregir el error de tipeo en el nombre de "Vlanck Widow" y modificarlo a "Black Widow"
for hero in avengers:
    if hero['nombre_superheroe'] == 'Vlanck Widow':
        hero['nombre_superheroe'] = 'Black Widow'

# f. Agregar los personajes de la lista auxiliar a la lista principal en caso de no estar cargados
aux_characters = ['Black Cat', 'Hulk', 'Rocket Racoonn', 'Loki']
for character in aux_characters:
    if not any(hero['nombre_superheroe'].lower() == character.lower() for hero in avengers):
        avengers.append({'nombre_superheroe': character, 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': ''})

# g. Mostrar todos los personajes que comienzan con C, P o S
characters_cps = [hero['nombre_superheroe'] for hero in avengers if hero['nombre_superheroe'][0] in ['C', 'P', 'S']]
print("Personajes que comienzan con C, P o S:")
for character in characters_cps:
    print(character)

# h. Cargar al menos 20 superhéroes a la lista
additional_heroes = [
    {'nombre_superheroe': 'Spider-Man', 'nombre_personaje': 'Peter Parker', 'grupo': '', 'anio_aparicion': 1962},
    {'nombre_superheroe': 'Doctor Strange', 'nombre_personaje': 'Stephen Strange', 'grupo': '', 'anio_aparicion': 1963},
    {'nombre_superheroe': 'Wolverine', 'nombre_personaje': 'Logan', 'grupo': '', 'anio_aparicion': 1974},
    {'nombre_superheroe': 'Vision', 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': 1968},
    {'nombre_superheroe': 'Falcon', 'nombre_personaje': 'Sam Wilson', 'grupo': '', 'anio_aparicion': 1969},
    {'nombre_superheroe': 'Ant-Man', 'nombre_personaje': 'Scott Lang', 'grupo': '', 'anio_aparicion': 1962},
    {'nombre_superheroe': 'Winter Soldier', 'nombre_personaje': 'Bucky Barnes', 'grupo': '', 'anio_aparicion': 2005},
    {'nombre_superheroe': 'Gamora', 'nombre_personaje': '', 'grupo': 'Guardianes de la galaxia', 'anio_aparicion': 1975},
    {'nombre_superheroe': 'Groot', 'nombre_personaje': '', 'grupo': 'Guardianes de la galaxia', 'anio_aparicion': 1960},
    {'nombre_superheroe': 'Rocket Raccoon', 'nombre_personaje': '', 'grupo': 'Guardianes de la galaxia', 'anio_aparicion': 1976},
    {'nombre_superheroe': 'Mantis', 'nombre_personaje': '', 'grupo': 'Guardianes de la galaxia', 'anio_aparicion': 1973},
    {'nombre_superheroe': 'Hank Pym', 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': 1962},
    {'nombre_superheroe': 'Jane Foster', 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': 1962},
    {'nombre_superheroe': 'Nick Fury', 'nombre_personaje': '', 'grupo': 'S.H.I.E.L.D.', 'anio_aparicion': 1963},
    {'nombre_superheroe': 'Quicksilver', 'nombre_personaje': 'Pietro Maximoff', 'grupo': '', 'anio_aparicion': 1964},
    {'nombre_superheroe': 'Loki', 'nombre_personaje': '', 'grupo': '', 'anio_aparicion': 1949},
    {'nombre_superheroe': 'Gambit', 'nombre_personaje': 'Remy LeBeau', 'grupo': 'X-Men', 'anio_aparicion': 1990},
    {'nombre_superheroe': 'Rogue', 'nombre_personaje': 'Anna Marie', 'grupo': 'X-Men', 'anio_aparicion': 1981},
    {'nombre_superheroe': 'Iceman', 'nombre_personaje': 'Bobby Drake', 'grupo': 'X-Men', 'anio_aparicion': 1963},
    {'nombre_superheroe': 'Colossus', 'nombre_personaje': 'Piotr Rasputin', 'grupo': 'X-Men', 'anio_aparicion': 1975}
]

avengers.extend(additional_heroes)

# Imprimir la lista completa de superhéroes
print("Lista completa de superhéroes:")
for hero in avengers:
    print(hero)
