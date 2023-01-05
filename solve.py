from taquin import Taquin, GameError
from astar import Astar
from bidirectional import Bidirectional
from heuristics import heuristic2, heuristic1, no_heuristic
import time
import numpy as np
import random
import signal

######## PARAMETERS FOR THE TEST #######

test_methods = [1,2,3,4] 
#1 for A* whith h1
#2 for A* whith h2
#3 for UCS=BFS
#4 for bidirectional search

number_tests = 5
check_frontier = True 
game_number = 15

timelimit = True
n_time = 600






def signal_handler(signum, frame):
        raise Exception("Timed out!")

def try_solve( a, check_frontier=False, timelimit : bool = False, n_time : int = 0):
    """function which takes as imput an astar or bidirectional object a,
    check_frontier: bool which determines if we compute the frontier or not,
    timelimit: bool if True there is a timelimit on the function call of solve,
    n_time: int, is the number of seconds of the limit.
    """
    if timelimit:
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(n_time)
        x=(-1,-1,-1)
        try:
            x = a.solve(check_frontier=check_frontier)
        except Exception:
            print("function timed out!")
    else:
        x = a.solve(check_frontier=check_frontier)
    return x

if np.sqrt(game_number + 1) % 1 != 0:
    raise ValueError('given n cannot create a game')
      
results = [[],[],[],[]]
times= [[],[],[],[]]
frontiers= [[],[],[],[]] 

############ Resolution and observation ###########
nb1,nb2,nb3,nb4 = (0,0,0,0)
for i in range(number_tests):  
    n = int(np.sqrt(game_number + 1))
    mix_n = random.randrange(1500,2500)
    taq = Taquin(n, True, solvable = 2000)
    if 1 in test_methods:
        a = Astar(root = taq, heuristic = heuristic1)
        x, t, fr = try_solve(a,check_frontier = check_frontier, timelimit = timelimit, n_time = n_time)
        if x == -1:
            nb1 +=1
        else:
            results[0].append(x)
            times[0].append(t)
            frontiers[0].append(fr)
    if 2 in test_methods:
        a = Astar(root = taq, heuristic = heuristic2)
        x, t, fr = try_solve(a,check_frontier = check_frontier, timelimit = timelimit, n_time = n_time)
        if x == -1:
            nb2 +=1
        else:
            results[1].append(x)
            times[1].append(t)
            frontiers[1].append(fr)
    if 3 in test_methods:
        a = Astar(root = taq, heuristic = no_heuristic)
        x, t, fr = try_solve(a,check_frontier = check_frontier, timelimit = timelimit, n_time = n_time)
        if x == -1:
            nb3 +=1
        else:
            results[2].append(x)
            times[2].append(t)
            frontiers[2].append(fr)
    if 4 in test_methods:
        a = Bidirectional(root = taq)
        x, t, fr = try_solve(a,check_frontier = check_frontier, timelimit = timelimit, n_time = n_time)
        if x == -1:
            nb4 +=1
        else:
            results[3].append(x)
            times[3].append(t)
            frontiers[3].append(fr)
        
        
if 1 in test_methods:
    print(f"the algorithm didn't find a solution in the time given {nb1} times")
    if number_tests != nb1:
        avg1 = np.mean(times[0])
        print(f"astar with h1 found solutions on average in {avg1} seconds")
if 2 in test_methods:
    print(f"the algorithm didn't find a solution in the time given {nb2} times")
    if number_tests != nb2:
        avg2 = np.mean(times[1])
        print(f"astar with h2 found solutions on average in {avg2} seconds")
if 3 in test_methods:
    print(f"the algorithm didn't find a solution in the time given {nb3} times")
    if number_tests != nb3:
        avg3 = np.mean(times[2])
        print(f"UCS found solutions on average in {avg3} seconds")
if 4 in test_methods:
    print(f"the algorithm didn't find a solution in the time given {nb4} times")
    if number_tests != nb4:
        avg4 = np.mean(times[3])
        print(f"Bidirectional found solutions on average in {avg4} seconds")  

if check_frontier:
    if 1 in test_methods and number_tests != nb1:
        avg1 = np.mean(frontiers[0])
        print(f"astar with h1 space complexity on average {avg1} ")
    if 2 in test_methods and number_tests != nb2:
        avg2 = np.mean(frontiers[1])
        print(f"astar with h2 space complexity on average  {avg2} ")
    if 3 in test_methods and number_tests != nb3:
        avg3 = np.mean(frontiers[2])
        print(f"UCS space complexity on average  {avg3} ")
    if 4 in test_methods and number_tests != nb4:
        avg4 = np.mean(frontiers[3])
        print(f"Bidirectional space complexity on average  {avg4} ")

if not timelimit:
    res = [ele for ele in results if ele != []]
    for i in range(len(res[0])):
        for j in range(len(res)-1):
            assert len(res[0][i]) == len(res[j+1][i]), "one methods output was wrong"


