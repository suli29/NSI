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

                rows.append(l);
            self.plateau.append(lignes)
        self.zonejeu.grille()

    def reverse(self):
        """
        Fonction qui permet d'inverser les cases de ligne en ligne et de colonne en colonne
        param i:(int) est la ligne qui est definie a 0
        param j:(int) est la colonne qui est definie a 3
        """
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.grillecase[ind][i],self.grillecase[ind][j]=self.grillecase[ind][j],self.grillecase[ind][i]
                i+=1
                j-=1

    def transpose(self):
        """
        Fonction qui permet de transposer la case a une autre case
        """
        self.grillecase=[list(t)for t in zip(*self.grillecase)]


    def fusioncase(self):
        """
        fonction qui permet de fusioner deux cases en une seule
        
        """
        self.fusion=False
        for i in range(4):
            for j in range(4 - 1):
                if self.grillecase[i][j] == self.grillecase[i][j + 1] and self.grillecase[i][j] != 0:
                    self.grillecase[i][j] *= 2
                    self.grillecase[i][j + 1] = 0
                    self.score += self.grillecase[i][j]
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
                if self.grillecase[i][j]!=0:
                    tab[i][a]=self.grillecase[i][j]
                    if a!=j:
                        self.addition=True
                    a+=1
        self.grillecase=tab
