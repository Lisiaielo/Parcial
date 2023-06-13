bitacora = [
    {"planeta": "Tatooine", "captura": "Jabba el Hutt", "recompensa": 1000},
    {"planeta": "Coruscant", "captura": "Greedo", "recompensa": 500},
    {"planeta": "Bespin", "captura": "Lando Calrissian", "recompensa": 800},
    {"planeta": "Endor", "captura": "Wicket W. Warrick", "recompensa": 300},
    {"planeta": "Hoth", "captura": "Han Solo", "recompensa": 2000}
]

# a. Mostrar los planetas visitados en el orden en que se realizaron las misiones
planetas_visitados = [mision["planeta"] for mision in bitacora]
print("Planetas visitados en orden:")
for planeta in planetas_visitados:
    print(planeta)

# b. Determinar cuántos créditos galácticos recaudó en total
total_creditos = sum(mision["recompensa"] for mision in bitacora)
print("Total de créditos galácticos recaudados:", total_creditos)

# c. Determinar el número de la misión en la que capturó a Han Solo y en qué planeta fue
for i, mision in enumerate(bitacora, 1):
    if mision["captura"] == "Han Solo":
        numero_mision = i
        planeta_captura = mision["planeta"]
        break

print("Número de la misión en la que capturó a Han Solo:", numero_mision)
print("Planeta de la captura de Han Solo:", planeta_captura)
