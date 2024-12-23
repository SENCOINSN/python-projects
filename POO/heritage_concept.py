class Film:
    def __init__(self,titre,realisateur,annee):
        self.titre = titre
        self.realisateur = realisateur
        self.annee = annee

    def info(self):
        print(f"le film {self.titre} est réalisé par {self.realisateur} en {self.annee}")
    

class FilmAction(Film):
    def __init__(self,titre,realisateur,annee):
        super().__init__(titre,realisateur,annee)
        self.genre = "action"
        
        
