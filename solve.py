from prompt_toolkit import prompt
from taquin import Taquin, GameError
from astar import Astar
from heuristic1 import Heuristic1
from heuristic2 import Heuristic2
from no_heuristic import No_heuristic

#x = prompt("1: astar")
x = 2
taq = Taquin(8, True, solvable = 1000)
taq.showmat()

if int(x) == 1:
    a = Astar(root = taq, heuristic = Heuristic1())
    try:
        x = a.solve()
        print('solution: ',x)
    except GameError as e:
        print('Problem: ', e)
        
if int(x) == 2:
    a = Astar(root = taq, heuristic= No_heuristic())
    try:
        x = a.solve()
        print('solution: ',x)
    except GameError as e:
        print('Problem: ', e)
    
    