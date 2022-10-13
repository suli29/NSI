import turtle
"""
turtle.reset()
turtle.home()
turtle.up()
turtle.goto(-50,-50)
turtle.down()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
"""
"""
def courbe_koch(n,cote):
    turtle.forward(cote)
    turtle.left(60)
    turtle.forward(cote)
    turtle.right(120)
    turtle.forward(cote)
    turtle.left(60)
    turtle.forward(cote)

courbe_koch(1,100)
"""

"""
def koch_recursive(n,cote):
    if n != 0:
        koch_recursive(n-1,cote/3)
        turtle.left(60)
        koch_recursive(n-1,cote/3)
        turtle.right(120)
        koch_recursive(n-1,cote/3)
        turtle.left(60)
        koch_recursive(n-1,cote/3)
    else:
        turtle.forward(cote)
    return

koch_recursive(2,100)
"""

"""
def flocon(n,c,cote):
    turtle.speed(800000)
    if n != 0:
        koch_recursive(c,cote)
        turtle.right(120)
        flocon(n-1,c,cote)
    else:
        koch_recursive(c,cote)
    return

flocon(2,2,400)
"""

"""
def coef(n,p):
    
    if p == 0 or n == p :
        return 1
    else:
        return coef(n-1,p-1) + coef(n-1,p)
            
for d in range(6):
    for w in range(d+1):
        print(coef(d,w), end=" ")
    print( )
"""


def recherche_dichotomique_recursive(t, v):
    debut = 0
    fin = len(t)-1
    if debut <= fin :
        milieu = (debut + fin) // 2
        if t[milieu] == v :
            return True 
        else:
            if t[milieu] > v :
                recherche_dichotomique_recursive(t[:milieu], v)
            else :
                recherche_dichotomique_recursive(t[milieu:], v)
    return False


print(recherche_dichotomique_recursive([0,2,1,5,2], 0))

