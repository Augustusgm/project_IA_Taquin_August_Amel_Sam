from taquin import Taquin, GameError
from prQueue import PrQueue
from collections import deque
from searchnode import SearchNode 
import time

class Astar :
    def __init__(self, root : Taquin,heuristic):
        self.root = SearchNode(root,father = None, action =None,nb_action = 0, h = heuristic)
        self.h = heuristic
        self.explored = set()
        self.frontier = PrQueue()
        #self.frontier.put(self.root)
        self.goal = self.root.state.goal()
     
    def solve(self):
        tic = time.perf_counter()
        #current = self.frontier.get()
        current = self.root
        i = -1
        while not current.state.isGoal(self.goal):
            i+=1
            if i%100000 == 0:
                print("taille frontiere ", self.frontier.size(), " taille extended ", len(self.explored))
                current.state.showmat()
                toc = time.perf_counter()
                print(f"You have been looking for the solution for {toc - tic:0.4f} seconds")
            self.explored.add(current.tobytes())
            for node in current.expand(self.h):
                if node.tobytes() not in self.explored:
                    self.frontier.put(node) 
            if self.frontier.empty():
                raise GameError(Exception("game has no solution"))
            current = self.frontier.get()
        solution = deque()
        while current.action is not None:
            solution.appendleft(current.action)
            current = current.father
        toc = time.perf_counter()
        print(f"Found solution in {toc - tic:0.4f} seconds")
        return solution


