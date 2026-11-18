etudiants = [
    ["Amina", 19, 14.5],
    ["Brice", 21, 12.0],
    ["Chloé", 20, 16.5],
]

print(etudiants[1][0])  # Brice

total = 0
for e in etudiants:
    total += e[2]
print(f"Moyenne générale : {total / len(etudiants):.2f}")  # 14.33