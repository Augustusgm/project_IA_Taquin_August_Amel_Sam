from prompt_toolkit import prompt
from taquin import Taquin, GameError
from astar import Astar
from heuristics import heuristic2, heuristic1, no_heuristic
import time
#x = prompt("1: astar")
x = 1
taq = Taquin(15, True, solvable = 1000)
taq.showmat()
tic = time.perf_counter()

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

toc = time.perf_counter()

print(f"solving with astar took {toc - tic:0.4f} seconds")
