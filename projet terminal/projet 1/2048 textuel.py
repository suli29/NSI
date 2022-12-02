plateau = [[2,0,4,0],[0,16,0,4],[0,8,0,32],[0,2,0,0]]

taille_plateau = 4

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
    cb = transpose(cb)  #permet de transposer
    cb = fusion_g(cb)   #permet de fusionner a gauche
    cb = transpose(cb) #permet de transposer
    
    return cb

def fusionbas(cb):
    """
    Fonction qui permet de fusionner vers le haut
    param cb : variable
    return : retourne la variable
    """
    cb = transpose(cb)  #permet de transposer
    cb = fusion_d(cb)   #permet de fusionner a droite
    cb = transpose(cb) #permet de transposer
    
    return cb
    
            
            
            

fusion_g(plateau)
fusionhaut(plateau)
fusion_d(plateau)
fusionhaut(plateau)
fusion_g(plateau)
affichage()
