from taquin import Taquin

def heuristic2(taquin : Taquin):
    value = 0
    for i in range(taquin.n):
        for j in range(taquin.n):
            cur = taquin.mat[i][j]
            if cur != 0: #prend pas en compte la case avail mais jsp si dois compter 
                official = divmod(cur,taquin.n)
                value = value + abs(i - official[0]) + abs(j - official[1] + 1)
    return value

def heuristic1(taquin : Taquin):
        valeur = 0
        for i in range(taquin.n):
            for j in range(taquin.n):
                cur = taquin.mat[i][j]
                if cur != taquin.mat[taquin.avail[0]][taquin.avail[1]]: #prend pas en compte la case avail mais jsp si dois compter 
                    official = list(divmod(cur,taquin.n))
                    if (i!=official[0]) or (j!=official[1]-1):
                        valeur += 1
        return valeur
                
def no_heuristic(taquin : Taquin):
        return 0