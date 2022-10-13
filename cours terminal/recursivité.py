def fct_recursive() :
    print("Je suis un appel de la fonction")
    fct_recursive()

def somme(n) :
    if n == 0 :
        return 0
    else :
        return n + somme(n-1)
    
def factorielle(n) :
	if n == 0 :
		return 1
	else :
		return n * factorielle(n-1)
	
def mystere(i,k):
    if i<=k :
    	print(i)
        boucle(i+1,k)

def maximum(t):
    if len(t) == 0:
        return -1
    elif len(t) == 1 :
        return t[0]
    else :
        return max(t[0], maximum(t[1:]))

def syracuse(u):
    print(u)
    if u > 1 :
        if u%2 == 0 :
            return syracuse(u//2)
        else :
            return syracuse(u*3 + 1)

def dentiste(texte) :
    voyelles = ["a","e","i","o","u","y"]
    if len(texte) == 1 :
        if texte[0] in voyelles :
            return texte[0]
    else :
        if texte[0] in voyelles :
            return texte[0] + dentiste(texte[1:])
        else :
            return dentiste(texte[1:])

def combine(t,t2):
    if len(t) > 0 and len(t2)> 0 :
        if t[0] < t2[0] :
            return [t[0]] + combine(t[1:],t2)
        else :
            return [t2[0]] + combine(t,t2[1:])
    elif len(t)>0:
        return t
    elif len(t2)>0 :
        return t2
    else :
        return []