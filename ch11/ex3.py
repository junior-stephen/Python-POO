import matplotlib.pyplot as plt

filieres = ["Génie Logiciel", "Réseaux", "Gestion", "Marketing", "Logistique"]
effectifs = [42, 35, 28, 31, 24]

plt.bar(filieres, effectifs, color="#2e75b6")
plt.title("Effectifs par filière")
plt.xlabel("Filière")
plt.ylabel("Nombre d'étudiants")
plt.show()