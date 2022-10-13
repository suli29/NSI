from random import randint

def creer_liste_aléatoire(nombre):
    liste = []
    for i in range(nombre):
        liste.append(randint(0, 50))
    return(liste)
    

def affiche1(liste):
    for i in range(len(liste)):
        print(liste[i])
        
        
def affiche2(liste):
    for element in liste:
        print(element)
        
        
def affiche3(liste):
    longeur = len(liste)
    if longeur==0:
        print("liste vide")
    else:
        for i in range(longeur-1):
            print(liste[i],end='-')
        print(liste[-1])

def appartient(element,liste):
    resultat = False
    i = 0
    while(not(resultat)and(i<len(liste))):
        if liste[i]==element:
            resultat= True
        i += 1
    return(resultat)

def inverse(liste):
    listeinv = []
    for i in range(len(liste)):
        listeinv = [liste[i]]+listeinv
    return(listeinv)

def inversebis(liste):
    listeinv = []
    for i in range(len(liste)-1,-1,-1):
        listeinv.append(liste[i])
    return(listeinv)

def listeAlea(nb,mini,maxi):
    liste =[]
    for i in range(nb):
        liste.append(randint(mini,maxi))
    return(liste)

def indice(element,liste):
    resultat = None
    i = 0
    while((resultat==None)and (i<len(liste))):
        if liste[i]==element:
            resultat = i
        i += 1 
    return(resultat)

def sommeListe(liste):
    somme = 0
    for i in range(len(liste)):
        somme += liste[i]
    return(somme)

def valeurMin(liste):
    minimum = liste[0]
    indice = 0
    for i in range(len(liste)):
        if liste[i]<minimum:
            minimum = liste[i]
            indice = i
    return(minimum, indice)

def valeurMax(liste):
    maximum = liste[0]
    indice = 0
    for i in range(len(liste)):
        if liste[i]>maximum:
            maximum = liste[i]
            indice = i
    return(maximum, indice)

def moyenne(liste):
    return(sommeListe(liste)/len(liste))

def triliste(liste):
    for i in range(len(liste)):
        maxi,imax = valeurMax(liste[i:])
        liste[i+imax] = liste[i]
        liste[i] = maxi
    return(liste)