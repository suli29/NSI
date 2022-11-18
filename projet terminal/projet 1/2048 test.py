from tkinter import *
import random 

class plateau:
    
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title = ('2048 test')
        self.plateau = []
        self.grille = [[0]*4 for i in range(4)]
        self.score = 0
        self.zonejeu = Frame(self.fenetre)
        
        for i in range(4):
                    lignes=[]
                    for j in range(4):
                        l=Label(self.zonejeu,text='',bg='white',
                        police=('arial',22,'bold'),width=4,height=2)
                        l.grille(ligne=i,colonne=j,padx=7,pady=7)
                        lignes.append(l);
                    self.plateau.append(lignes)
                    self.zonejeu.grille()

    def inverser(self):
        """
        Fonction qui permet d'inverser les cases de ligne en ligne et de colonne en colonne
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

    def transposer(self):
        """
        Fonction qui permet de transposer la case a une autre case
        """
        self.case=[list(t)for t in zip(*self.case)]


    def fusioncase(self):
        """
        fonction qui permet de fusioner deux cases en une seule
        
        """
        self.fusion=False
        for i in range(4):
            for j in range(4 - 1):
                if self.case[i][j] == self.case[i][j + 1] and self.case[i][j] != 0:
                    self.case[i][j] *= 2
                    self.case[i][j + 1] = 0
                    self.score += self.case[i][j]
                    self.fusion = True
                    
    def additioncase(self):
        """
        Fonction qui additionne deux memes cases en une case plus grande
        param temps:(int) tableau 
        param a:(int) variable defini a 0
        """
        self.addition=False
        tab=[[0] *4 for i in range(4)]
        for i in range(4):
            a=0
            for j in range(4):
                if self.case[i][j]!=0:
                    tab[i][a]=self.case[i][j]
                    if a!=j:
                        self.addition=True
                    a+=1
        self.case=tab

