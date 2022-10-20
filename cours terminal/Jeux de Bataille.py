from TP_File import *
import random
   
VAL_CARTE = ['1','2','3','4','5','6','7','8','9','10','V','D','R','AS']
COL_CARTE = ['P','T','C','H']

def in_file(x,f):
    """
    Fonction qui revoie True si x est dans la file f
    param x (): element present ou non dans f
    param f (File1/File2) : File contenant ou non x
    return (bool) : Renvoie True si x est dans f, False sinon
    """
    if type(f) == File :
        if x in f.file :
            return True
        else :
            return False
    elif type(f) == File2 :
        if f.tete == x :
            return True
        elif f.queue != None :
            return in_file(x,f.queue)
        else :
            return False
    else :
        return False
        
def comp(c1,c2) :
    """
    Fonction de comparaison entre deux cartes
    param c1 : (tuple) Carte 1
    param c2 : (tuple) Carte 2
    return : Renvoie
                    -1 si => c1 < c2
                    1  si => c1 > <2
                    0  si => c1 == c2
    
    """
    print(c1[0],c2[0],'test')
    if VAL_CARTE.index(c1[0]) < VAL_CARTE.index(c2[0]) :
        return -1
    elif VAL_CARTE.index(c1[0]) > VAL_CARTE.index(c2[0]) :
        return 1
    else :
        return 0
                    
def creer_jeu():
    """
    Fonction qui crée un jeu aléatoire
    return a,b (File) Deux files contenant 26 cartes chacunes
    """
    i = 0
    val_carte = ['1','2','3','4','5','6','7','8','9','10','V','D','R','AS']
    col_carte = ['P','T','C','H']
    f1 = File()
    f2 = File()
    while i < 52 :
        val = random.randint(0,len(val_carte)-1)
        col = random.randint(0,len(col_carte)-1)
        carte = (val_carte[val],col_carte[col])
        if in_file(carte,f1) == False and in_file(carte,f2) == False  :
            if i%2 == 0 :
                f1.enfile(carte)
            else :
                f2.enfile(carte)
            i+=1
    return f1,f2
            
def tour(f1,f2) :
    """
    Foncton qui simule un tour de bataille
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    """
    i = f1.defile()
    j = f2.defile()
    res = comp(i,j)
    if res == 1 :
        f1.enfile(i)
        f1.enfile(j)
    elif res == -1:
        f2.enfile(i)
        f2.enfile(j)
    else :
        print('bataille')
        if f1.taille() > 3 and f2.taille() > 3 :
            bataille(i,j,f1,f2)
        else :
            if f1.taille() < 3 :
                f1.vide_file()
            else :
                f2.vide_file()
                
            
def bataille(c1,c2,f1,f2) :
    """
    Fonction simulant un tour de bataille
    param c1 : (tuple) Carte n°1 égale a c2
    param c2 : (tuple) Carte n°1 égale a c1
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2    
    """
    bataille_tab= []
    while comp(c1,c2) == 0:
        bataille_tab += [f1.defile()]
        bataille_tab += [f2.defile()]
        c1 = f1.defile()
        c2 = f2.defile()
        bataille_tab += [c1]
        bataille_tab += [c2]
    if comp(c1,c2) == 1 :
        for i in bataille_tab():
            f1.enfile()
    if comp(c1,c2) == -1 :
        for i in bataille_tab():
            f2.enfile()
        
        
        
def est_fini(f1,f2):
    """
    Fonction qui détermine si le jeu est fini
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    return (bool): renvoie True si le jeu est fini, False sinon.
    """
    if f1.est_vide() == True:
        return True 
        
    elif f2.est_vide() == True:
        return True 
    else :
        return False
        
    

def game(f1,f2):
    """
    Fonction simulant le jeu de la bataille
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    """
    while not est_fini(f1,f2) :
        tour(f1,f2)
        
f1,f2 = creer_jeu()