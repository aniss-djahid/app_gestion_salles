class Salle:
    def __init__(self, code, libelle, type, capacite):
        self.code = code
        self.libelle = libelle
        self.type = type
        self.capacite = capacite

    def afficher_infos(self):
        print("code :", self.code)
        print("libellé :", self.libelle)
        print("type :", self.type)
        print("capacité :", self.capacite)