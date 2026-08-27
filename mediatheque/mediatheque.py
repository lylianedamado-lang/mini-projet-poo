from mediatheque.adherent import Adherent
from mediatheque.erreurs import (
    DocumentIndisponible,
    TropDEmprunts,
    DocumentInconnu,
)


class Mediatheque:
    """Gère les documents, les adhérents et les prêts."""

    def __init__(self, nom):
        self.nom = nom
        self.documents = []
        self.adherents = []
        self._compteur_numero = 0

    def ajouter_document(self, document):
        self.documents.append(document)
        return document

    def inscrire(self, nom):
        self._compteur_numero += 1
        adherent = Adherent(nom, self._compteur_numero)
        self.adherents.append(adherent)
        return adherent

    def _trouver_document(self, code):
        for doc in self.documents:
            if doc.code == code:
                return doc
        raise DocumentInconnu(f"Aucun document avec le code {code}")

    def _trouver_adherent(self, numero):
        for adh in self.adherents:
            if adh.numero == numero:
                return adh
        raise DocumentInconnu(f"Aucun adherent avec le numero {numero}")

    def emprunter(self, numero, code):
        adherent = self._trouver_adherent(numero)
        document = self._trouver_document(code)

        if not document.disponible:
            raise DocumentIndisponible(f"{document.titre} est deja emprunte")
        if not adherent.peut_emprunter():
            raise TropDEmprunts(f"{adherent.nom} a deja 3 emprunts")

        document.disponible = False
        adherent.emprunts.append(document)
        return document

    def rendre(self, numero, code):
        adherent = self._trouver_adherent(numero)
        document = self._trouver_document(code)

        document.disponible = True
        if document in adherent.emprunts:
            adherent.emprunts.remove(document)
        return document

    def rechercher(self, mot):
        mot = mot.lower()
        return [doc for doc in self.documents if mot in doc.titre.lower()]

    def documents_disponibles(self):
        return [doc for doc in self.documents if doc.disponible]

    def emprunts_de(self, numero):
        adherent = self._trouver_adherent(numero)
        return adherent.emprunts
