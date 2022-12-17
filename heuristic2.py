from taquin import Taquin

class Heuristic2:
    
    def __init__(self):
        self.valeur = 0
    
    def value(self, taquin : Taquin):
        value = self.valeur
        for i in range(taquin.n):
            for j in range(taquin.n):
                cur = taquin.mat[i][j]
                if cur != 0: #prend pas en compte la case avail mais jsp si dois compter 
                    official = divmod(cur,taquin.n)
                    value = abs(i - official[0]) + abs(j - official[1]+1)
        return value
                