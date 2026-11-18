note_cc = 12
note_examen = 15
coef_examen = 0.6
moyenne = note_cc * (1 - coef_examen) + note_examen * coef_examen
print(f"Moyenne : {moyenne:.2f} / 20")  # 13.80