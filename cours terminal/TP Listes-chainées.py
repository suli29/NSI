class Liste : #Creation d'une classe "Liste"
    
    def __init__(self,element,queue=None):
        """
        Fonction qui prend en compte deux parametre
        param element : (attribut) le contenu de la liste chainée
        param queue : (attribut) le pointeur qui pointe vers le suivent
        
        return : (liste) liste chainée avec les elements
        """
        self.element = element
        self.queue = queue
        
    def est_vide(self):
        """
        Renvoie Vrai si la liste est vide.
        :return: (bool) Vrai si la liste est vide, Faux sinon.
        :CU: aucune

        Exemple:
        >>> l1 = Liste()
        >>> l1.est_vide()
        True
        >>> l2 = Liste([1,2,3])
        >>> l2.est_vide()
        False
        """
        if self.element == None:
            if self.queue != None:
                return True and self.queue.est_vide()
            else:
                return True
        else:
            return False
            
    def ajouter_element_queue(self, valeur):
        """
        Fonction qui ajoute un maillon à la liste chaînée.
        param valeur : (int)
        """
        if self.queue == None:
            self.queue = Liste(valeur)
        else:
            self.queue.ajouter_element_queue(valeur)
        
    def longueur(self):
        """
        Fonction qui renvoi la longueur de la queue
        """
        if self.queue == None:
            return 1
        else:
            return 1+self.queue.longueur()
            
    def extrait_element(self,element):
        if self.element == element:
            return 0
        else:
            if self.queue == None:
                return
            else:
                return 1+ self.queue.extrait_element(element)
        
    def __repr__(self):
        s = '[ '
        s = s+ str(self.element)
        queue = self.queue
        while queue != None:
            s = s +','
            s= s + str(queue.element)
            queue = queue.queue
        return s + ' ]'
    

        
    def __add__(self,Liste2):
        self.ajoute_element_queue(Liste2.element)
        queue = Liste2.element
        while queue != None:
            self.ajoute_element_queue(queue.element)
            queue = queue.queue
        
        
        
        
        
        
    
m3 = Liste(3)
m2 = Liste(2, m3)
m1 = Liste(1, m2)