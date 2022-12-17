from taquin import Taquin

def heuristic2(taquin : Taquin):
    n = taquin.n()
    value = 0
    for i in range(n):
        for j in range(n):
            cur = taquin.mat[i][j]
            if cur != 0: #prend pas en compte la case avail mais jsp si dois compter 
                official = divmod(cur,n)
                value = value + abs(i - official[0]) + abs(j - official[1] + 1)
    return value

def heuristic1(taquin : Taquin):
    n = taquin.n()
    valeur = 0
    for i in range(n):
        for j in range(n):
            cur = taquin.mat[i][j]
            if cur != taquin.mat[taquin.avail[0]][taquin.avail[1]]: #prend pas en compte la case avail mais jsp si dois compter 
                official = list(divmod(cur,n))
                if (i!=official[0]) or (j!=official[1]-1):
                    valeur += 1
    return valeur
                
def no_heuristic(taquin : Taquin):
        return 0