                                                                            #TP Pile

class Pile():
       
    def __init__(self):
        """
        Fonction qui renvoie pile = tableau vide
        param pile:(list) liste pile
        """
        self.pile=[]
        
    def empile(self,elem):
        """
        Fonction qui ajoute un element a la pile
        param elem:(int) element qu'on ajoute a la pile
        return :(list) liste avec element qu'on a ajoute
        """
        #self.pile+ = [elem]
        self.pile.append(elem)
        
    def depile(self):
        """
        Fonction qui enleve l'element du dessus de la liste
        return : (liste) renvoie la liste avec l'element retire de la liste
        """
        if self.est_vide():
            return None
        else:
            return self.pile.pop()
        
    def est_vide(self):
        """Methode calculant la longueur de la pile"""
        return self.pile == []
    
    def top(self):
        """Methode renvoyant l'element au dessus de la pile"""
        return self.pile[-1]
    
    def taille (self):
        """Methode permettant de connaitre la taille de la pile"""
        return len(self.pile)
    
    def __repr__(self):
        """
        Fonction qui affiche la pile
        return :(int) La liste ecrit les uns au dessus des autres sous forme d'entier
        """
        long = len(self.pile)-1
        s = ' '
        while long >=0:
            s+=str(self.pile[long])+ '\n'
            long = long-1
        return s

def bien_parenthese(chaine):
    
    """
    Fonction qui verifie si une parenthese ou un crochet se ferme
    Param texte : (str) texte a verifier
    return :(bool) renvoie true si les parenthese ou crochet sont bien ferme
                                    ou false si les parenthese ou crochet ne sont pas bien ferme
    """
    p = Pile()
    for i in chaine :
        if i == '(' or i == '[':
            p.empile(i)
        elif i == ')' or i == ']':
            dernier = p.depile()
            if dernier == False :
                return False
            else:
                if i == ')' :
                    if dernier != '(':
                        return False
                else:
                    if dernier != '[':
                        return False
        else:
            pass
    return p.est_vide()
    
def calculatrice(calcul):
    """
    Fonction qui permet de faire des calculs simple mais pose l'opérateur après les deux opérandes.
    """
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
  
def tri_pile(pile):
    pile_trie = Pile()
    pile_tmp = Pile()
    #s = pile.depile()
    #pile_trie.empile(s)
    pile_trie.empile(pile.depile())
    while pile.est_vide() == False :
        if pile.top() > pile_trie.top() :
            while pile_trie.est_vide() == False and pile.top() > pile_trie.top() :
                pile_tmp.empile(pile_trie.depile())
            pile_trie.empile(pile.depile())
            while pile.tmp.est_vide() != False :
                pile_trie.empile(pile_tmp.depile())
        else :
            pile_trie.empile(pile.depile())
    while pile_trie.est_vide() == False :
        pile_tmp.empile(pile_trie.depile())
    while pile_tmp.est_vide() == False :
        pile.empile(pile_tmp.depile())
        
        
        
