from liste import valeurMax,listeAlea

def triliste(liste):
    for i in range(len(liste)):
        maxi,imax = valeurMax(liste[i:])
        liste[i+imax] = liste[i]
        liste[i] = maxi
    return(liste)

def  trilistebis(liste):
    liste_a_trier = list(liste)
    liste_triee = list()
    while liste_a_trier != []:
        maxi = liste_a_trier[0]
        for element in liste_a_trier[1:]:
            if element>maxi:
                maxi = element
                liste_triee.append(maxi)
                liste_a_trier.remove(maxi)
    return(liste_triee)
    
liste_non_triee = listeAlea(10,0,50)
print(liste_non_triee)
liste_triee = triliste(liste_non_triee) 
print(liste_triee)

def  trilistebis(liste):
    liste_a_trier = list(liste)
    liste_triee = list()
    while liste_a_trier != []:
        mini = liste_a_trier[0]
        for element in liste_a_trier[1:]:
            if element>mini:
                mini = element
                liste_triee.append(mini)
                liste_a_trier.remove(mini)
    return(liste_triee)
