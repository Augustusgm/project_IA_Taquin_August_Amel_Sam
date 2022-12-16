from prompt_toolkit import prompt
from taquin import Taquin, GameError
from astar import Astar

#x = prompt("1: astar")
x = 1
taq = Taquin(15, True, solvable = 1000)
taq.showmat()

if int(x) == 1:
    a = Astar(root = taq)
    try:
        x = a.solve()
        print('solution: ',x)
    except GameError as e:
        print('Problem: ', e)
    
    