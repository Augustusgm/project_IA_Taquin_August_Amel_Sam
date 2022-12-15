from taquin import Taquin

class Heuristic1:
    
    def __init__(self):
        self.valeur = 0
    
    def value(self, taquin : Taquin):
        valeur = self.valeur
        for i in range(taquin.n):
            for j in range(taquin.n):
                cur = taquin.mat[i][j]
                if cur != taquin.avail: #prend pas en compte la case avail mais jsp si dois compter 
                    official = divmod(cur,taquin.n)
                    official[1]-=1
                    if (i!=official[0]) or (j!=official[1]):
                        valeur += 1
        return valeur
                
                
        