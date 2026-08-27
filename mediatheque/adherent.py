class Adherent:
    """Un adhérent de la médiathèque, qui peut emprunter des documents."""

    MAX_EMPRUNTS = 3

    def __init__(self, nom, numero):
        self.nom = nom
        self.numero = numero
        self.emprunts = []

    def peut_emprunter(self):
        return len(self.emprunts) < self.MAX_EMPRUNTS

    def __len__(self):
        return len(self.emprunts)

    def __str__(self):
        return f'Adherent {self.nom} (n {self.numero}) - {len(self.emprunts)} emprunt(s)'
