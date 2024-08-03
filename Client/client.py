class Client:
    def __init__(self, nom, prenom, adresse, ville, code_postal, pays, comptes=None):
        
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.ville = ville
        self.code_postal = code_postal
        self.pays = pays
        self.comptes = comptes if comptes is not None else []
        
    
    #Méthode d'affichage pour le déboggage
    def __repr__(self):
        return f"{self.prenom} {self.nom} habite à {self.adresse}, {self.ville}, {self.code_postal}, {self.pays}"
    
    #Méthode pour ouvrir un compte
    def ouvrir_compte(self, compte):
        self.comptes.append(compte)
        