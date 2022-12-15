from taquin import Taquin

class Heuristic1:
    
    def __init__(self):
        self.value = 0
    
    def value(self, taquin : Taquin):
        value = self.value
        for i in range(taquin.n):
            for j in range(taquin.n):
                cur = taquin.mat[i][j]
                if cur != taquin.avail: #prend pas en compte la case avail mais jsp si dois compter 
                    official = divmod(cur,taquin.n)
                    official[1]-=1
                    if (i!=official[0]) or (j!=official[1]):
                        self.value = self.value + 1
        return self.value
                
                
        