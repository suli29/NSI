import random # importation du module random afin de pouvoir afficher aleatoirement
import copy # importation du module copy afin de pouvoir creer des liens

taille_plateau = 4 # permet de changer la taille du plateau
print(" Les touche du jeux sont [z] pour haut, [s] pour bas, [q] pour gauche et [d] pour droite . ")
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

def fusionligne1(ligne):
    """
    Fonction qui permet de fusionner la ligne
    param j :(int) ordonnee soit la colonne
    param i :(int) abscisse soit la ligne
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
    param i : abscisse soit la ligne
    param cb : variable qui signifie le plateau actuel
    return : retourne la variable cb
    """
    for i in range (taille_plateau):
        cb[i] = fusionligne1(cb[i])    
    return cb

def reverse(ligne):
    new = []
    for i in range (taille_plateau -1,-1,-1):
        new.append(ligne[i])
    return new

def fusion_d(cb):
    """
    Fonction qui permet de fusionner vers la droite
    param i : abscisse soit la ligne
    param cb : variable qui signifie le plateau actuel
    return : retourne la variable cb
    """
    for i in range (taille_plateau):
        cb[i] = reverse(cb[i])
        cb[i] = fusionligne1(cb[i])
        cb[i] = reverse(cb[i])
    return cb
            
            
            
def transpose(cb):
    """
    Fonction qui permet transposer i vers j ou inversement
    param j :(int) ordonnee soit la colonne
    param i :(int) abscisse soit la ligne
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
    param cb : variable
    return : retourne la variable
    """
    cb = transpose(cb)  # permet de transposer
    cb = fusion_g(cb)   # ermet de fusionner a gauche
    cb = transpose(cb) # permet de transposer
    
    return cb

def fusionbas(cb):
    """
    Fonction qui permet de fusionner vers le haut
    param cb : variable
    return : retourne la variable
    """
    cb = transpose(cb)  # permet de transposer
    cb = fusion_d(cb)   # permet de fusionner a droite
    cb = transpose(cb) # permet de transposer
    
    return cb

def nouvellevaleur():
    """
    Fonction qui permet d'ajouter une nouvelle valeur aleatoirement dans le plateau
    
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
    Fonction qui permet de stopper le jeu lorsqu on atteint 2048
    """
    for ligne in plateau:
        if 2048 in ligne:
            return True
    return False

def plus_mouvements():
    """
    Fonction qui permet de stopper le jeu lorsque l'on a rempli le plateau et que l'on ne peut plus faire de deplacement
    """
    temp_plateau1 = copy.deepcopy(plateau)
    temp_plateau2 = copy.deepcopy(plateau)
    
    temp_plateau1 = fusionbas(temp_plateau1)
    if temp_plateau1 == temp_plateau2:
        temp_plateau1 = fusionhaut(temp_plateau1)
        if temp_plateau1 == temp_plateau2:
            temp_plateau1 = fusion_g(temp_plateau1)
            if temp_plateau1 == temp_plateau2:
                temp_plateau1 = fusion_d(temp_plateau1)
                if temp_plateau1 == temp_plateau2:
                    return True
    return False
    
    
    
    
plateau = []
for i in range(taille_plateau):
    ligne = []
    for j in range(taille_plateau):
        ligne.append(0)
    plateau.append(ligne)

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
    deplacement = input("ou voulez vous allez :  ")
    
    validInput = True
    
    temp_plateau = copy.deepcopy(plateau)
    
    if deplacement == "d" or deplacement == "D":
        plateau = fusion_d(plateau)
    elif deplacement == "z" or deplacement == "Z":
        plateau = fusionhaut(plateau)
    elif deplacement == "q" or deplacement == "Q":
        plateau = fusion_g(plateau)
    elif deplacement == "s"  or deplacement == "S":
        plateau = fusionbas(plateau)
    else:
        validInput = False
    
    if not validInput:
        print("Veuillez reessayer l'entrée n'est pas valide")
    else:
        if plateau == temp_plateau:
            print(affichage())
        else:
            if gagne():
                affichage()
                print("Vous avez gagné")
                fin_du_jeu = True
            else:
                ajout_nouvelle_valeur()
                            
                affichage()
                
                if plus_mouvements():
                    print("Plus de mouvement possible, vous avez perdu !")
                    fin_du_jeu = True

affichage()