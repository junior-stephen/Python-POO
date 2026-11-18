from etudiant import Etudiant

class Groupe:
    def __init__(self):
        self.etudiants = []

    def ajouter(self, etudiant):
        self.etudiants.append(etudiant)

    def moyenne_generale(self):
        total = 0
        for etudiant in self.etudiants:
            total += etudiant.moyenne()
        return total / len(self.etudiants)