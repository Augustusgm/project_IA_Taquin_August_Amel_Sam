from taquin import Taquin

class No_heuristic:
    
    def __init__(self):
        self.value = 0
    
    def value(self, taquin : Taquin):
        self.value = 0
        return self.value