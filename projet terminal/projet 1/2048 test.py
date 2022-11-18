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
                self.grillecase[ind][i],self.grillecase[ind][j]=self.grillecase[ind][j],self.grillecase[ind][i]
                i+=1
                j-=1

    def transposer(self):
        """
        Fonction qui permet de transposer la case a une autre case
        """
        self.grillecase=[list(t)for t in zip(*self.grillecase)]
        
    def compressergrille(self):
        self.compresse=False
        temp=[[0] *4 for i in range(4)]
        for i in range(4):
            cnt=0
            for j in range(4):
                if self.grillecase[i][j]!=0:
                    temp[i][cnt]=self.grillecase[i][j]
                    if cnt!=j:
                        self.compresse=True
                    cnt+=1
        self.grillecase=
