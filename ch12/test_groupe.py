from etudiant import Etudiant
from groupe import Groupe

groupe = Groupe()
groupe.ajouter(Etudiant("Amina", 12.0, 15.5))
groupe.ajouter(Etudiant("Brice", 10.0, 11.0))
groupe.ajouter(Etudiant("Chloé", 14.0, 16.0))

print(f"Moyenne générale : {groupe.moyenne_generale():.2f} / 20")

meilleur = groupe.etudiants[0]
for etudiant in groupe.etudiants:
    if etudiant.moyenne() > meilleur.moyenne():
        meilleur = etudiant

print(f"Meilleure moyenne : {meilleur.nom} ({meilleur.moyenne():.2f} / 20)")