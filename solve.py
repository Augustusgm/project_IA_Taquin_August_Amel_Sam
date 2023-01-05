from taquin import Taquin, GameError
from astar import Astar
from bidirectional import Bidirectional
from heuristics import heuristic2, heuristic1, no_heuristic
import time
import numpy as np
import random

#PARAMETERS FOR THE TEST

test_methods = [1,2,3,4] 
#1 for A* whith h1
#2 for A* whith h2
#3 for UCS=BFS
#4 for bidirectional search

number_tests = 50
check_frontier = True 
game_number = 8






if np.sqrt(game_number + 1) % 1 != 0:
    raise ValueError('given n cannot create a game')
      
results = [[],[],[],[]]
times= [[],[],[],[]]
frontiers= [[],[],[],[]]

for i in range(number_tests):  
    n = int(np.sqrt(game_number + 1))
    mix_n = random.randrange(1500,2500)
    taq = Taquin(n, True, solvable = 2000)
    if 1 in test_methods:
        a = Astar(root = taq, heuristic = heuristic1)
        x, t, fr = a.solve(check_frontier = check_frontier)
        results[0].append(x)
        times[0].append(t)
        frontiers[0].append(fr)
    if 2 in test_methods:
        a = Astar(root = taq, heuristic = heuristic2)
        x, t, fr = a.solve(check_frontier=check_frontier)
        results[1].append(x)
        times[1].append(t)
        frontiers[1].append(fr)
    if 3 in test_methods:
        a = Astar(root = taq, heuristic = no_heuristic)
        x, t, fr = a.solve(check_frontier = check_frontier)
        results[2].append(x)
        times[2].append(t)
        frontiers[2].append(fr)
    if 4 in test_methods:
        a = Bidirectional(root = taq)
        x, t, fr = a.solve(check_frontier = check_frontier)
        toc = time.perf_counter()
        results[3].append(x)
        times[3].append(t)
        frontiers[3].append(fr)
        
        
if 1 in test_methods:
    avg1 = np.mean(times[0])
    print(f"astar with h1 found solutions on average in {avg1} seconds")
if 2 in test_methods:
    avg2 = np.mean(times[1])
    print(f"astar with h2 found solutions on average in {avg2} seconds")
if 3 in test_methods:
    avg3 = np.mean(times[2])
    print(f"UCS found solutions on average in {avg3} seconds")
if 4 in test_methods:
    avg4 = np.mean(times[3])
    print(f"Bidirectional found solutions on average in {avg4} seconds")  
    
if check_frontier:
    if 1 in test_methods:
        avg1 = np.mean(frontiers[0])
        print(f"astar with h1 space complexity on average {avg1} ")
    if 2 in test_methods:
        avg2 = np.mean(frontiers[1])
        print(f"astar with h2 space complexity on average  {avg2} ")
    if 3 in test_methods:
        avg3 = np.mean(frontiers[2])
        print(f"UCS space complexity on average  {avg3} ")
    if 4 in test_methods:
        avg4 = np.mean(frontiers[3])
        print(f"Bidirectional space complexity on average  {avg4} ")

res = [ele for ele in results if ele != []]
for i in range(len(res[0])):
    for j in range(len(res)-1):
        assert len(res[0][i]) == len(res[j+1][i]), "one methods output was wrong"
