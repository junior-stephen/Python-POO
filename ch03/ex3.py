etudiants = [("Amina", 12, 14.75), ("Brice", 10, 13.5)]

for nom, credits, note in etudiants:
    print(f"{nom:<8}{credits:>5}{note:>10.2f} / 20")