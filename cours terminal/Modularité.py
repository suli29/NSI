def plus_grand_que(a,b):
    """
    Fonction permettant de savoir quelle valeur entre a et b est la plus grande
    param a : (int) valeur à comparer
    param b : (int) valeur à comparer
    return :(str) element le plus grand
    """
    if a > b:
        return True
    else:
        return False
    return


from math import sqrt
def Pythagore(cote1,cote2,hypothenuse):
    """
    Fonction qui determine sur un triangle de coté : cote1,cote2,hypothenuse est
    rectangle
    param cote1 : (int) cote 1 du triangle
    param cote2 : (int) cote 2 du triangle
    param hypothenuse : (int) cote le plus grand des 3 cote
    return: (str) renvoi 'le triangle est rectangle' si le triangle est rectangle et renvoi 'le triangle n'est pas rectangle' si le triangle n'est pas rectangle
    """
    if sqrt(cote1**2+cote2**2) == hypothenuse**2:
        return"le triangle est rectangle"
    else:
        return"le triangle n'est pas rectangle"
    return


def somme(t):
    """
    Fonction qui additionne tous les elements d'un tableau et renvoi la somme
    param t : (int) tableau dans lequel il ya tous les elements a additionner
    return : (int) renvoi la somme de tous les elements additionne 
    """
    liste_somme = 0
    for nb in t:
        liste_somme = liste_somme + nb
    return liste_somme


def recherche_dichotomique(t, v):

    """
    Fonction qui applique la recherche dichotomique dans un tableau
    param t : (list) Tableau où l on va rechercher une valeur
    param v : (int/str/float) valeur à retrouver
    return : (int) Renvoie l'indice de la position de val, -1 si val n'est pas dans le tableau
    """
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


def dentiste(texte):
    """
    Fonction qui renvoi un texte ne contenant que les voyelles de texte, dans l'ordre
    param texte : (str) mot dans lequel on renverra que les voyelles
    return : (str) renvoi les voyelles du mot
    """
    s =''    
    voyelle = ['a','e','i','o','u','y']
    for i in texte : 
        if i in voyelle :
            s += i
    return s


if __name__=="__main__":
    doctest.testmod(verbose=True)