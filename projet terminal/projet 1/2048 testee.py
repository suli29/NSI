for i in range(4):
            lignes=[]
            for j in range(4):
                l=Label(self.zonejeu,text='',bg='azure4',
                police=('arial',22,'bold'),width=4,height=2)
                l.grille(ligne=i,colonne=j,padx=7,pady=7)

                rows.append(l);
            self.plateau.append(lignes)
        self.zonejeu.grille()

    def reverse(self):
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.grillecase[ind][i],self.grillecase[ind][j]=self.grillecase[ind][j],self.grillecase[ind][i]
                i+=1
                j-=1

    def transpose(self):
        self.grillecase=[list(t)for t in zip(*self.)]