plateau = [[2,0,4,0],[0,16,0,4],[0,8,0,32],[0,2,0,0]]

def affichage():
    
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







































affichage()







                    
                    
                    

                



