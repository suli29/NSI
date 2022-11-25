plateau = [[2,0,4,0],[0,16,0,4],[0,8,0,32],[0,2,0,0]]

def affichage():
    for ligne in plateau:
        c ="|"
        for element in ligne:
            if element == 0:
                c += "|"
            else :
                c += str(element) + "|"
        print(c)
    print()
                    
                    
affichage()

                    
                    
                    

                



