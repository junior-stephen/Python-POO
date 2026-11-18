def compter_reussites(notes, seuil=10):
    return sum(1 for note in notes if note >= seuil)

def classer(note):
    if note < 10:
        return "ÉCHEC"
    elif note >= 14:
        return "MENTION"
    return "PASSABLE"

def a_progresse(note_cc, note_examen):
    return "PROGRESSION" if note_examen > note_cc else "PAS DE PROGRESSION"

notes = [8, 12, 15, 17, 10, 6]
print(compter_reussites(notes))
for note in notes:
    print(note, classer(note))

for cc, exam in zip([12, 10, 14], [15, 9, 14]):
    print(a_progresse(cc, exam))