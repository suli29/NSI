from tkinter import *
import random
import tkinter as tk

#creation class plateau
class Plateau:
    
    #cree une fenetre 
    fen = tk.Tk()

    #fond noir du 2048
    canvas = Canvas(fen, width=600, height=600, background='black')
    #permet d'afficher le canvas
    canvas.pack()


    
    def __init__(self):
        self.fen.title = ('2048 test')
        self.plateau = []
        self.grille = [[0]*4 for i in range(4)]
        self.score = 0
        self.zonejeu = Frame(self.fen)
        
        for y in range(4):
                    t=[]
                    
                    for j in range(4):
                        l=Label(self.zonejeu,text='',bg='white',font=('arial',22,'bold'),width=4,height=2)
                        self.grille(y[i][j],padx=7,pady=7)
                        
                        t.append(l);
                    self.plateau.append(t)
                    self.zonejeu.grille()

    def echange(self):
        """
        Fonction qui permet d'echanger une case avec une autre
        param i:(int) est la ligne qui est definie a 0
        param j:(int) est la colonne qui est definie a 3
        """
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.case[ind][i],self.case[ind][j]=self.case[ind][j],self.case[ind][i]
                i+=1
                j-=1


    def fusioncase(self):
        """
        fonction qui permet de fusionner deux cases en une seule
        
        """
        self.fusion=False
        for i in range(4):
            for j in range(3):
                if self.case[i][j] == self.case[i][j + 1] and self.case[i][j] != 0:
                    self.case[i][j] *= 2
                    self.case[i][j + 1] = 0
                    self.score += self.case[i][j]
                    self.fusion = True
                    
                    
                    
    def identique(self,pos1,pos2):
        """
        Fonction permettant de verifier si les deux cases sont identiques
        """
     
        
        if self.grille[pos1] == self.grille[pos2]:
            self.additioncase == True
        else:
            self.additioncase == False

p = Plateau()
p.echange()


    
"""
fen.mainloop()
"""
