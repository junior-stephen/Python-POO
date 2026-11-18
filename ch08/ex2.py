classe = [
    {"nom": "Amina", "note_cc": 12.0, "note_examen": 15.5},
    {"nom": "Brice", "note_cc": 10.0, "note_examen": 11.0},
    {"nom": "Chloé", "note_cc": 14.0, "note_examen": 16.0},
]

total = 0
for etudiant in classe:
    moyenne = etudiant["note_cc"] * 0.4 + etudiant["note_examen"] * 0.6
    print(f"{etudiant['nom']} : {moyenne:.2f} / 20")
    total += moyenne

print(f"Moyenne générale : {total / len(classe):.2f} / 20")