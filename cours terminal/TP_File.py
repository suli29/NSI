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
    
class File_2:
    
    def __init__(self,elem,suite) :
        self.element = elem
        self.queue = suite

    def enfile(self,elem):
        self.queue = File(self.elem,self.suivant)
        self.elem = elem 
        
    def est_vide(self):
        if self.element == None:
            if self.queue != None :
        return True and self.queue.est_vide():
            else:
                return True
        else:
            return False
