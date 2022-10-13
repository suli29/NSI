# 2. Classe Auteur
class Auteur :
    def __init__(self,nom_aut,naissance_aut,deces_aut) :
        self.nom = nom_aut
        self.naissance = naissance_aut
        self.deces = deces_aut
        if  type(deces_aut)==int:
            print(self.deces)
        else :
            False
A = Auteur('Moi',1584,4879)
# 3. Classe Livre

class Livre :
    def __init__(self, titre_livre,genre_livre,Auteur) :
        self.titre = titre_livre
        self.genre = genre_livre
        self.auteur = Auteur
    
L = Livre('rien','Policier',1852)
# 4. Classe bibliothèque

class bibliotheque :
    def __init__(self, type_de_rayon) :
        self.TypeRayon = type_de_rayon
        self.livres_dans_blibliotheque = []
    def disponible(self,nom_livre) :
        for livre in self.livres_dans_blibliotheque :
            if livre.titre == nom_livre:
                return True
            return False
    def ajout(self, nom_livre):
        if nom_livre.genre == self.rayon :
            self.livres_dans_blibliotheque.append(livre)
            return "Livre ajouté"
        else :
            return "Le livre ne peut pas etre ajouté" 
    def pret_livre(self, livre):
        if livre.genre == self.rayon :
            if self.disponible(livre.titre) == True :
                num_element = 0
                trouver = False
                while num_element < len(self.livres_dans_blibliotheque) and trouver == False :
                    liste_livre = self.livres_dans_bibliotheque
                    livre_pos_courante = liste_livre[num_element]
                    titre_livre_pos_courante = livre_pos_courante.titre
                    #if livre.titre == self.livres_dans_blibliotheque[num_element].titre
                    if livre.titre == titre_livre_pos_courante :
                        l = liste_livre.pop(num_element)
                        # l = self.livres_dans_bibliotheque.pop(num_element)
                        trouver = True
                    num_element+=1
                if trouver == True :
                    return l
        return False
    
    
    
    
    
