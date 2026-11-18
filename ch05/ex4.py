notes_cc = [12, 10, 14]
notes_examen = [15, 9, 14]

for i in range(len(notes_cc)):
    if notes_examen[i] > notes_cc[i]:
        print(f"Étudiant {i + 1} : PROGRESSION")
    else:
        print(f"Étudiant {i + 1} : PAS DE PROGRESSION")