import matplotlib.pyplot as plt

evaluations = [f"Éval {i}" for i in range(1, 11)]
notes = [12.5, 14.0, 13.5, 16.0, 15.5, 11.0, 12.0, 14.5, 15.0, 16.5]

plt.plot(evaluations, notes)
plt.title("Évolution des notes")
plt.xlabel("Évaluation")
plt.ylabel("Note (/20)")
plt.show()