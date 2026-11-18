score = 40
semaine = 0

while score <= 60:
    score = score * 1.03
    semaine += 1

print(f"{semaine} semaines nécessaires (score : {score:.2f})")  # 14 semaines