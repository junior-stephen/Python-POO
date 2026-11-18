bulletins = [
    (10.5, 17.5, 14.2),
    (8.0, 16.0, 12.1),
    (11.0, 15.0, 13.0),
]

for note_min, note_max, moyenne in bulletins:
    print(f"Moyenne {moyenne} — écart : {note_max - note_min:.2f}")