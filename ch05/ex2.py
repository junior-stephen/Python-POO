notes = [8, 12, 15, 17, 10, 6]

for note in notes:
    if note < 10:
        print(note, "ÉCHEC")
    elif note >= 14:
        print(note, "MENTION")
    else:
        print(note, "PASSABLE")