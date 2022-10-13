"""
#1 Syntaxe Python
#1.
le mot clé pour definir une fonction est def
#2.
Les deux types de boucles sont for et while
#3.
Le mot return veut dire retourner une valeur a la fin de la fonction
#4.
La fonction print() permet d afficher une valeur


#2 Rappel 1ère
#2.1. Plus grand que :
def plus_grand_que(a,b):
    if a > b:
        return True
    else:
        return False
    return

#2.2. Pythagore :
from math import sqrt
def Pythagore(cote1,cote2,hypothenuse):
    if sqrt(cote1**2+cote2**2) == hypothenuse**2:
        return"le triangle est rectangle"
    else:
        return"le triangle n'est pas rectangle"
    return

#2.3. Tableaux :
def somme(t):
    liste_somme = 0
    for nb in t:
        liste_somme = liste_somme + nb
    return liste_somme
    

#2.4. Fonction de tri :
le tri par selection veut dire tri par comparaison

le tri par insertion veut dire inserer dans chaque liste pour a la fin tout soit trié
Prenons comme exemple la suite de nombre suivante : 9, 2, 7, 1 que l on veut trier en ordre croissant avec l algorithme du tri par insertion : 1er tour : 9 | 2, 7, 1
-> à gauche la partie triée du tableau, à droite la partie non triée.

#2.5. Recherche dichotomique :

#1
La recherche dichotomique est un algorithme de recherche pour trouver la position d un élément dans un tableau trié.

#2


#3
def recherche_dichotomique(t, v):
    
    Fonction qui applique la recherche dichotomique dans un tableau
    param tableau : Tableau où l on va rechercher une valeur
    param valeur : valeur à retrouver
    return : Renvoie l'indice de la position de val, -1 si val n'est pas dans le tableau
    
    debut = 0
    fin = len(t)-1
    while  debut != fin:
        milieu = (debut+fin)//2
        if t[milieu] > v :
            fin = milieu-1
        elif t[milieu] < v :
            debut = milieu+1
        elif t[milieu] == v :
            return milieu
    return -1

#2.6. Dentiste

#1
le type de valeur de retour de cette fonction est en str

#2
def dentiste(texte):
    s =' '    
    voyelle = ['a','e','i','o','u','y']
    for i in texte : 
        if i in voyelle :
            s += i
    return s 
           
           
def dentiste_range(texte):
    s =''    
    voyelle = ['a','e','i','o','u','y']
    for i in range(len(texte)) :
        if texte[i] in voyelle :
            s += texte[i]
    return s

def dentiste_while(texte):
    s =''    
    voyelle = ['a','e','i','o','u','y']
    i = 0
    while i<= (len(texte)-1):
        if texte[i] in voyelle:
            s += texte[i]
        i = i+1
    return s

#3

print(dentiste('texte'))

"""
"""

                                                                        #Rappel premiere CONDITION

                        #Exercice 1

chaine = 'NSI'
var = 6 
var2 = 16
print(chaine)
#1.Que se passe-t-il ? Pourquoi ?
#Vu que l'on n'a pas appeler la variable, il ne s'affiche rien
#2.Que se passe-t-il lorsqu'on appelle la variable chaine ? Pourquoi ce résultat ?
#Lorsque l'on appelle la variable, ça renvoie 'NSI', car on a defini chaine = 'NSI'
#3.Re-exécuter le programme. Que se passe-t-il lorsqu'on appelle la variable chaine ? Pourquoi ?
#Lorsque l'on appelle la variable, ça renvoie '7', car on a redefini chaine = '7'

                        #Exercice 2

chaine2 = '123'
chaine3 = '14'
chaine4 = 'az'
chaine5 = 'abbbbbbbbbbbb'

#1.Tester chaine2 < chaine3. Que se passe t-il ? Pourquoi ?
print(chaine2 < chaine3)
#Lorsqu'on appelle la variable print(chaine2 < chaine3), ca renvoit True car la chaine sont des caractere dyscographique
#2.Tester chaine4 < chaine5. Que se passe t-il ? Pourquoi ?
print(chaine4 < chaine5)
#Lorsqu'on appelle la variable print(chaine4 < chaine5), ca renvoit False car la chaine sont des caractere dyscographique
#3.Tester len(chaine4) < len(chaine5). Que se passe t-il ? Pourquoi ?
print(len(chaine4) < len(chaine5))
#Lorsqu'on appelle la variable print(len(chaine4) < len(chaine5)), ca renvoit True car ca compare la longueur des chaines

                        #Exercice 3: Communiquer avec l'utilisateur

#1.Que s'est-il passé ? Que vaut var ?
#Ca print 5, var vaut rien
#2.Quel est le type de la variable var ? (Utilisez type(var))
#le type de var est <class 'NoneType'>
"""

                    #Rappel premiere Boucle for
#Exercice 1

for _ in range(5): 
    print("Je suis un bloc d'instruction de la boucle for") 

for i in range(4): 
    print("Je suis la phrase numéro ",i) 

for ind in range(45): 
    print(ind)

#Expliquez ce que fait la fonction range(n)
    #La fonction range permet de créer une liste.
#Que permet selon-vous la variable '_' ?
    #'_' permet de ne pas reutiliser cette variable
#Que valent i et ind ? Pourquoi ?
    # i et ind valent un int car on ne peut pas mettre de str dans une boucle for
for _ in range(2,5): 
    print("Je suis un bloc d'instruction de la boucle for") 
 
for i in range(2,4): 
    print("Je suis la phrase numéro ",i) 
 
for ind in range(10,45,5): 
    print(ind)

#Expliquez ce que fait la fonction range(n,m)
    #
#Expliquez ce que fait la fonction range(n,m,o)
    #
#Que valent i et ind ? Pourquoi ?
    #

