from abc import ABC, abstractmethod


class Document(ABC):
    """Classe de base abstraite : un document de la médiathèque."""

    def __init__(self, titre, annee, code):
        self._titre = titre
        self._code = code
        self.annee = annee
        self.disponible = True

    @property
    def titre(self):
        return self._titre

    @property
    def code(self):
        return self._code

    @abstractmethod
    def duree_pret(self):
        """Nombre de jours de prêt autorisé (dépend du type de document)."""
        ...

    def __str__(self):
        return f'"{self._titre}" ({self.annee})'

    def __eq__(self, autre):
        return isinstance(autre, Document) and self._code == autre._code



class Livre(Document):
    """Un livre : se prête pour 21 jours."""

    def __init__(self, titre, annee, code, auteur, nb_pages):
        super().__init__(titre, annee, code)
        self.auteur = auteur
        self.nb_pages = nb_pages

    def duree_pret(self):
        return 21

    def __str__(self):
        return f'Livre {super().__str__()} - a rendre sous {self.duree_pret()} jours'


class DVD(Document):
    """Un DVD : se prête pour 7 jours."""

    def __init__(self, titre, annee, code, realisateur, duree_min):
        super().__init__(titre, annee, code)
        self.realisateur = realisateur
        self.duree_min = duree_min

    def duree_pret(self):
        return 7

    def __str__(self):
        return f'DVD {super().__str__()} - a rendre sous {self.duree_pret()} jours'
