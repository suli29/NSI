class Pile:
    def __init__(self):    
        self.pile = []
    def empile(self,nb):
        """
        Ajoute un nombre mis en paramètre a la fin de la pile
        :param nb : (int)
        """
        self.pile += [nb]
    def depile(self):
        """
        Enlève le dernier élément de la liste
        """
        if len(self.pile) != 0:
            return self.pile.pop()
        else:
            return None
    def est_vide():
        return self.pile == []
    def taille(self):
         """
         Retourne la taille du tableau
         """
        return len(self.pile)

def bien_parenthese(chaine):
    p = Pile()
    for i in chaine:
        #Ouvrante
        if i == "(" or i == "[":
            p.empile(i)
        #fermante
        elif i == ")" or i == "]":
            dernier = p.depile()
            if dernier == False:
                return False
            else:
                if i ==")":
                    if dernier != "(":
                        return False
                else:
                    if dernier == "[":
                        return False
        #Autres cas
        else:
            pass
    return p.est_vide()


def calculatrice(calcul):
    pile = Pile()
    for nb in calcul:
        if nb in '0123456789' :
            pile.empile(nb)
        elif nb == '+' or nb =='-' or nb =='*':
            nb1 = pile.depile()
            nb2 = pile.depile()
            if nb == '+' :
                res = int(nb1) + int(nb2)
            pile.empile(res)
        else :
            pass
    return pile.depile()

    def __repr__(self):
        long = len(self.pile)-1
        s = ''
        while long >= 0:
            s += str(self.pile[long])+'\n'
            long= long-1
        return s

    
