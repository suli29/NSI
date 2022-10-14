class File:
    def __init__(self) -> None:
        self.file = []
  
    def enfile( ):
        self.file=[nv]+self.file
    
    def defile(self):
        if self.est_vide():
            return None
        else:
            return self.file.pop()
        
    def est_vide(self):
        return self.file == []
    
    def top(self):
        return self.file[-1]
    
    def taille (self):
        return len(self.file)
    
    def ajout_element(self):
        if self.taille()>=7:
            return "sorry"
        else:
            self.enfile(elem)
            
    def vide_file(self):
        for i in self.file:
            self.defile(i)
    
class File2:
    
    def __init__(self,elem, suite):
        self.element = elem
        self.suivant = suite
    
    def enfile(self,elem):
        self.suivant = File2(self.elem, self.suivant)
        self.element = elem        
        
      def defile(self):
        if self.est_vide():
            return False
        elif self.suivant.suivant == None:
            val = self.suivant.elem
            self.suivant = None
            return val
        elif self.suivant == None:
            val = self.elem
            self.elem = None
            return val
        else:
            self.suivant.defile()
            
        
    def est_vide(self):
        if self.nombre == None:
            if self.suivant != None:
                return True and self.suivant.est_vide()
            else:
                return True
        else:
            return False
    
    def top(self):
        return self.file[-1]
    
    def taille (self):
        return len(self.file)
    
    
