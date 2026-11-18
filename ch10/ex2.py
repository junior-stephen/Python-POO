def mention(note, seuil_passable=10, seuil_bien=14):
    if note < seuil_passable:
        return "AJOURNÉ"
    elif note >= seuil_bien:
        return "BIEN"
    else:
        return "PASSABLE"

print(mention(8), mention(12), mention(15))  # AJOURNÉ PASSABLE BIEN