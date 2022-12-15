import random # importation du module random afin de pouvoir afficher aleatoirement
import copy # importation du module copy afin de pouvoir creer des liens

taille_plateau = 4 # permet de changer la taille du plateau
print(" Les touches du jeux sont [z] pour haut, [s] pour bas, [q] pour gauche et [d] pour droite . ")
print("        ")

def affichage():
    """
    Fonction qui permet d'afficher le plateau de jeu
    param ligne: ligne du plateau
    param element: numero dans la case
    param larg: largeur du tableau
    param NumSpace: Nombre d'espace
    """
    larg = plateau[0][0]
    for ligne in plateau:
        for element in ligne:
            if element > larg :
                larg = element
    
    NumSpaces = len(str(larg))
                
    
    for ligne in plateau:
        c ="|"
        for element in ligne:
            if element == 0:
                c += " " * NumSpaces +"|"
            
            else :
                c += (" " *(NumSpaces - len(str(element)))) + str(element) + "|"
        print(c)
    print()

def fusionligne(ligne):
    """
    Fonction qui permet de fusionner la ligne
    param ligne : ligne du plateau 
    return : retourne la ligne
    """
    for j in range(taille_plateau -1):
        for i in range(taille_plateau -1, 0, -1):
            if ligne[i -1] == 0:
                ligne[i-1] = ligne[i]
                ligne[i] = 0
    for i in range(taille_plateau -1):
        if ligne[i] == ligne[i+1]:
            ligne[i] *= 2
            ligne[i+1] = 0
            
    for i in range(taille_plateau -1, 0, -1):
        if ligne[i-1] == 0:
            ligne[i-1] == ligne[i]
            ligne[i] == 0
    return ligne
            

def fusion_g(cb):
    """
    Fonction qui permet de fusionner vers la gauche
    param cb : variable qui signifie le plateau actuel
    return : retourne la variable cb
    """
    for i in range (taille_plateau):
        cb[i] = fusionligne(cb[i])    
    return cb

def reverse(ligne):
    new = []
    for i in range (taille_plateau -1,-1,-1):
        new.append(ligne[i])
    return new

def fusion_d(cb):
    """
    Fonction qui permet de fusionner vers la droite
    param cb : variable qui signifie le plateau actuel
    return : retourne la variable cb
    """
    for i in range (taille_plateau):
        cb[i] = reverse(cb[i])
        cb[i] = fusionligne(cb[i])
        cb[i] = reverse(cb[i])
    return cb
            
            
            
def transpose(cb):
    """
    Fonction qui permet transposer i vers j ou inversement
    param cb : variable qui signifie le plateau actuel
    return : retourne la variable cb
    """
    for j in range(taille_plateau):
        for i in range(j, taille_plateau):
            if not i == j:
                temp = cb[j][i]
                cb[j][i] = cb[i][j]
                cb[i][j] = temp
    return cb
            
def fusionhaut(cb):
    """
    Fonction qui permet de fusionner vers le haut
    param cb : variable plateau actuel
    return : retourne la variable
    """
    cb = transpose(cb)  # permet de transposer
    cb = fusion_g(cb)   # permet de fusionner a gauche
    cb = transpose(cb) # permet de transposer
    
    return cb

def fusionbas(cb):
    """
    Fonction qui permet de fusionner vers le haut
    param cb : variable plateau actuel
    return : retourne la variable
    """
    cb = transpose(cb)  # permet de transposer
    cb = fusion_d(cb)   # permet de fusionner a droite
    cb = transpose(cb) # permet de transposer
    
    return cb

def nouvellevaleur():
    """
    Fonction qui permet d ajouter une nouvelle valeur aleatoirement dans le plateau
    
    """
    if random.randint(1, 8) ==  1:
        return 4
    else:
        return 2
    
def ajout_nouvelle_valeur():
    """
    Fonction qui nous permet d'ajouter une valeur dans le plateau afin que lorsqu'on deplace le jeu une valeur apparaisse aleatoirement
    """
    ligneNum = random.randint(0, taille_plateau -1)
    colonneNum = random.randint(0, taille_plateau -1)
    
    while not plateau[ligneNum][colonneNum] == 0:
        ligneNum = random.randint(0, taille_plateau -1)
        colonneNum = random.randint(0, taille_plateau -1)
        
    plateau[ligneNum][colonneNum] = nouvellevaleur()

def gagne():
    """
    Fonction qui permet de stopper le jeu lorsqu on atteint 2048 dans une case
    """
    for ligne in plateau:
        if 2048 in ligne:
            return True
    return False

def plus_fusions_possible():
    """
    Fonction qui permet de stopper le jeu lorsque lon a rempli le plateau et que lon ne peut plus faire de deplacement
    """
    temp_plateau1 = copy.deepcopy(plateau) #copy et garde en memoire plateau dans un dictionnaire
    temp_plateau2 = copy.deepcopy(plateau) #copy et garde en memoire plateau dans un dictionnaire
    
    temp_plateau1 = fusionbas(temp_plateau1)
    if temp_plateau1 == temp_plateau2:
        temp_plateau1 = fusionhaut(temp_plateau1)
        if temp_plateau1 == temp_plateau2:
            temp_plateau1 = fusion_g(temp_plateau1)
            if temp_plateau1 == temp_plateau2:
                temp_plateau1 = fusion_d(temp_plateau1)
                if temp_plateau1 == temp_plateau2:
                    return True  #retourne True si le plateau temporaire 1 est egale au plateau temporaire 2
    return False  #retourne False si le plateau temporaire 1 est egale a la fusion haut du plateau temporaire 1    
    
    
    
plateau = []   #creation d'une liste vide
for i in range(taille_plateau): #pour i dans la taille du plateau
    ligne = [] #ligne vaut liste vide
    for j in range(taille_plateau): #pour j dans la taille du plateau
        ligne.append(0) #ajoute 0 dans la liste vide
    plateau.append(ligne) #ajoute la ligne dans le plateau

numRequis = 2 
while numRequis > 0:
    ligneNum = random.randint(0, taille_plateau -1) 
    colonneNum = random.randint(0, taille_plateau -1)
    
    if plateau[ligneNum][colonneNum] == 0:
        plateau[ligneNum][colonneNum] = nouvellevaleur()
        numRequis -= 1
        
fin_du_jeu = False

affichage()

while not fin_du_jeu: 
    deplacement = input("Où voulez-vous allez :  ") #demande quel deplacement le joueur veut faire
    
    validInput = True  #valide input si la touche correspond aux bonnes touches
    
    temp_plateau = copy.deepcopy(plateau) #permet de garder en memoire plateau dans un dictionnaire
    
    if deplacement == "d" or deplacement == "D":  #assigne la touche D ou d
        plateau = fusion_d(plateau) #appel la fonction fusion_d pour deplacer les lignes vers la droite
    elif deplacement == "z" or deplacement == "Z":   #assigne la touche Z ou z
        plateau = fusionhaut(plateau) #appel la fonction fusionhaut pour deplacer les lignes vers le haut
    elif deplacement == "q" or deplacement == "Q":   #assigne la touche Q ou q
        plateau = fusion_g(plateau) #appel la fonction fusion_g pour deplacer les lignes vers la gauche
    elif deplacement == "s"  or deplacement == "S":    #assigne la touche S ou s
        plateau = fusionbas(plateau) #appel la fonction fusionbas pour deplacer les lignes vers le bas
    else:
        validInput = False #ne valide pas input si la touche ne correspond pas aux bonnes touches
    
    if not validInput:
        print("Entrée NON-Valide")  #renvoi Entree NON Valide car la touche inserer ne correspond pas au touche valide
    else:
        if plateau == temp_plateau:
            print(affichage())
        else:
            if gagne():                                 #
                affichage()                            #
                print("Vous avez gagné")      #arrete le jeu car le joueur a atteint 2048 dans une case
                fin_du_jeu = True               #
            else:                                        #
                ajout_nouvelle_valeur()        #sinon ajouter une nouvelle valeur
                            
                affichage()
                                        
                if plus_fusions_possible():                                                #
                    print("Plus de fusion possible, vous avez PERDU !")     #arrete le jeu car il n'y a plus de fusion possible
                    fin_du_jeu = True                                                        #
                    

affichage()
