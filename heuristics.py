from taquin import Taquin

def heuristic2(taquin : Taquin):
    """gives the manhattan distance from current state to the goal. the divmod operator gives the position in which each state should be in to efficiently compute the distance"""
    n = taquin.n()
    value = 0
    for i in range(n):
        for j in range(n):
            cur = taquin.mat[i][j]
            if cur != 0: #prend pas en compte la case avail mais jsp si dois compter 
                official = divmod(cur-1,n)
                value = value + abs(i - official[0]) + abs(j - official[1])
    return value

def heuristic1(taquin : Taquin):
    """method which returns the value for h1 :number of displaced tiles """
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
    """method to use uniform cost search """
    return 0