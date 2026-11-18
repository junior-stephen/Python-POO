def calculer_moyenne_classe(classe):
    total = 0
    for e in classe:
        total += e["note_cc"] * 0.4 + e["note_examen"] * 0.6
    return total / len(classe)

classe = [
    {"nom": "Amina", "note_cc": 12.0, "note_examen": 15.5},
    {"nom": "Brice", "note_cc": 10.0, "note_examen": 11.0},
]
print(f"{calculer_moyenne_classe(classe):.2f}")  # 12.35