plateau = [[2,0,4,0],[0,16,0,4],[0,8,0,32],[0,2,0,0]]

def affichage():
    """
    Fonction qui permet d'afficher le plateau de jeu
    
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
    















affichage()







                    
                    
                    

                



