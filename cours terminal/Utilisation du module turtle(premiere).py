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

#1 Quelle est la figure dessinée ici ?
# un carré

#2 Décrire le but de ces fonctions
# reset() : Réinitialise le dessin
# home() : Place le stylo en position (0,0)
# up() : le stylo monte
# goto(x,y) :  va a une coordonnées x y
# forward(x) : le trait monte sur le dessin
# left(x) : le trait va a gauche 
# right(x) : le trait va a droite
"""
"""
#3 Transformer ce bout de code en une fonction, écrire aussi la documentation de celle-ci
def carre():
"""
"""
    Fonction qui dessine un carre   
"""
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

print(carre())
"""
#Exercice 2
"""
def triangle_equilateral():
    turtle.reset()
    turtle.home()
    turtle.up()
    turtle.goto(-50,-50)
    turtle.down()
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(60)
print(triangle_equilateral())
"""
#Exercice 3
"""
def hexagone():
    for i in range(6):
        turtle.forward(60)
        turtle.left(60)
    
hexagone()

def rose():
    for i in range(4):
        for i in range(6):
             hexagone()
             turtle.left(90)
        
rose()
"""
#Exercice 5

def triforce():
    for i in range(3):
        for i in range(3):
            turtle.left(120)
            turtle.forward(60)
            
            
        
triforce()