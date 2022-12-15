from prompt_toolkit import prompt
from taquin import Taquin, GameError
from astar import Astar

#x = prompt("1: astar")
x = 1
taq = Taquin(8, True)
taq.showmat()

if int(x) == 1:
    a = Astar(root = taq)
    try:
        x = a.solve()
    except GameError as e:
        print('Problem: ', e)
    else:
        print('solution: ',x)
    
    