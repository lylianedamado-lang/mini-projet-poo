class MediathequeError(Exception):
    """Erreur de base de la médiathèque. Toutes les autres en héritent."""
    pass


class DocumentIndisponible(MediathequeError):
    """Le document demandé est déjà emprunté."""
    pass


class TropDEmprunts(MediathequeError):
    """L'adhérent a déjà 3 emprunts en cours."""
    pass


class DocumentInconnu(MediathequeError):
    """Aucun document ne correspond à ce code."""
    pass
