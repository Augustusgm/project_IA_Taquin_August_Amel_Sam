import taquin from Taquin

class Heuristic1:
    
    def __init__(self):
        self.value = 0
    
    def value(self, taquin : Taquin):
        for i in range(self.n):
            for j in range(self.n):
                cur = self.mat[i][j]
                if cur != taquin.avail: #prend pas en compte la case avail mais jsp si dois compter 
                    official = divmod(cur,taquin.n)
                    official[1]-=1
                    self.value = self.value + abs(i - official[0]) + abs(j - official[1])
        return self.value
                