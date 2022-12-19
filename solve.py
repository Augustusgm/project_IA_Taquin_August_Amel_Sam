from prompt_toolkit import prompt
from taquin import Taquin, GameError
from astar import Astar
from heuristics import heuristic2, heuristic1, no_heuristic
import time
import numpy as np
import sys

#x = prompt("1: astar")
x = 0
game_number = 15
if np.sqrt(game_number + 1) % 1 != 0:
          raise ValueError('n given cannot create a game')
n = int(np.sqrt(game_number + 1))
taq = Taquin(n, True, solvable = 1000)
taq.showmat()
#tic = time.perf_counter()

if int(x) == 1:
    a = Astar(root = taq, heuristic = heuristic2)
    try:
        x = a.solve()
        print('solution: ',x)
    except GameError as e:
        print('Problem: ', e)
elif int(x) == 2:
    a = Astar(root = taq, heuristic= no_heuristic)
    try:
        x = a.solve()
        print('solution: ',x)
    except GameError as e:
        print('Problem: ', e)
        
taquin= Taquin(4,False)
taquin.mat[0][0]= 12
taquin.mat[0][1]= 1
taquin.mat[0][2]= 2
taquin.mat[0][3]= 15
taquin.mat[1][0]= 11
taquin.mat[1][1]= 6
taquin.mat[1][2]= 5
taquin.mat[1][3]= 8
taquin.mat[2][0]= 7
taquin.mat[2][1]= 10
taquin.mat[2][2]= 9
taquin.mat[2][3]= 4
taquin.mat[3][0]= 0
taquin.mat[3][1]= 13
taquin.mat[3][2]= 14
taquin.mat[3][3]= 3
taquin.showmat()

a = Astar(root = taquin, heuristic = heuristic2)
x = a.solve()
print('solution: ',x)
#toc = time.perf_counter()

#print(f"solving with astar took {toc - tic:0.4f} seconds")
