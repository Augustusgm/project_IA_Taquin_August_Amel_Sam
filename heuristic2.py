import taquin from Taquin

class Heuristic1:
    
    def __init__(self):
        self.value = 0
    
    def value(self, taquin : Taquin):
        for i in range n:
            for j in range n:
                cur = self.mat[i][j]
                if cur != np.where(self.mat == 0): #prend pas en compte la case avail mais jsp si dois compter 
                    official = divmod(cur,taquin.n)
                    official[1]-=1
                    value = value + abs(i - official[0]) + abs(j - official[1])
        return value
                