class File:
    def __init__(self) -> None:
        self.file = []
  
    def enfile( ):
        self.file=[nv]+self.file
    
    def defile(self):
        """
        Fonction qui enleve l'element du dessus de la liste
        return : (liste) renvoie la liste avec l'element retire de la liste
        """
        if self.est_vide():
            return None
        else:
            return self.file.pop()
        
    def est_vide(self):
        """Methode calculant la longueur de la file"""
        return self.file == []
    
    def top(self):
        """Methode renvoyant l'element au dessus de la file"""
        return self.file[-1]
    
    def taille (self):
        """Methode permettant de connaitre la taille de la file"""
        return len(self.file)
    
