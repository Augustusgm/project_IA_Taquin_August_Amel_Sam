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
                    value = value + abs(i - official[0]) + abs(j - official[1])
        return value
                