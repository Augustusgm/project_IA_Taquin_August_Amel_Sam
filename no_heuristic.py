from taquin import Taquin

class No_heuristic:
    
    def __init__(self):
        self.valeur = 0
    
    def value(self, taquin : Taquin):
        return self.valeur