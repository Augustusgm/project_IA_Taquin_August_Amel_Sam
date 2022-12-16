from prompt_toolkit import prompt
from taquin import Taquin, GameError
from astar import Astar
from ucs import UCS
from heuristic1 import Heuristic1

#x = prompt("1: astar")
x = 1
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
    a = UCS(root = taq)
    try:
        x = a.solve()
        print('solution: ',x)
    except GameError as e:
        print('Problem: ', e)
    
    