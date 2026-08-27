"""Démonstration de la médiathèque."""
from mediatheque.mediatheque import Mediatheque
from mediatheque.documents import Livre, DVD
from mediatheque.erreurs import DocumentIndisponible, TropDEmprunts, DocumentInconnu


def main():
    mediatheque = Mediatheque("Mediatheque de Dakar")

    mediatheque.ajouter_document(
        Livre("L Aventure ambigue", 1961, "L001",
              auteur="Cheikh Hamidou Kane", nb_pages=191)
    )
    mediatheque.ajouter_document(
        DVD("Camp de Thiaroye", 1988, "D001",
            realisateur="Sembene Ousmane", duree_min=147)
    )

    awa = mediatheque.inscrire("Awa Diop")

    # Un emprunt qui réussit
    pret = mediatheque.emprunter(awa.numero, "L001")
    print(pret)
    print("Nombre d'emprunts de Awa :", len(awa))

    # Un emprunt impossible : le livre est déjà pris
    try:
        mediatheque.emprunter(awa.numero, "L001")
    except DocumentIndisponible as err:
        print("Impossible :", err)

    # Recherche insensible à la casse
    print("\nRecherche 'aventure' :")
    for doc in mediatheque.rechercher("aventure"):
        print("  trouve :", doc)

    # Polymorphisme : une seule boucle, un affichage correct pour chaque type
    print("\nDocuments disponibles :")
    for doc in mediatheque.documents_disponibles():
        print(" ", doc)

    # On rend le livre, il redevient disponible
    mediatheque.rendre(awa.numero, "L001")
    print("\nApres avoir rendu le livre :")
    for doc in mediatheque.documents_disponibles():
        print(" ", doc)


if __name__ == "__main__":
    main()
