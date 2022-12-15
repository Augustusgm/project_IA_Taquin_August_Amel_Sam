import taquin from Taquin

class Heuristic1:
    
    def __init__(self):
        self.value = 0
    
    def value(self, taquin : Taquin):
        for i in range n:
            for j in range n:
                cur = self.mat[i][j]
                if cur != taquin.avail: #prend pas en compte la case avail mais jsp si dois compter 
                    official = divmod(cur,taquin.n)
                    official[1]-=1
                    if (i!=official[0]) or (j!=official[1]):
                        value = value + 1
        return value
                
                
        