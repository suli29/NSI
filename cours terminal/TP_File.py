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
    
