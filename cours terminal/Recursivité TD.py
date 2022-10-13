"""
                        #TD Récursivité
#1. Application du cours
#1. 1. Fonction somme :
def somme(n) :
    if n == 0 :
        return 0
    else :
        return n + somme(n-1)
    
print(somme(5))
'6 appels'
print(somme(n))
'n+1 appels'

#1. 2. Fonction factorielle :
def factorielle(n):
    if n == 0 :
        return 1
    else :
        return n * factorielle(n-1)

print(factorielle(4))
'4 appels'

#2. TD
#2. 1. Fonction mystère :
def mystere(i,k):
    if i<=k :
        print(i)
        mystere(i+1,k)
        
print(mystere(0,10))
'la fonction mystere affiche les chiffres compris entre i et k'
'si i est strictement inferieur a k'

#2. 2. Nombre de chiffre d'un nombre :
def nb_chiffre(n) :
    if n < 10 :
        return 1
    else :
        return 1 + nb_chiffre(n//10)
    
print(nb_chiffre(201))
"""
#2. 3. Maximum d'un tableau :
def maximum(t):
    if len(t) == 1 :
        return t[0]
    elif len(t)==0 :
        return "Le tableau est vide"
    else :
        return max(t[0], maximum(t[1:]))
    
print(maximum([1,4,7]))

#3. Bonus :
#3. 1. Suite de Syracuse :

