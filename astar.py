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
        self.frontier.put(self.root)
        self.goal = self.root.state.goal()
     
    def solve(self, check_frontier = False):
        maxfrontier = 1
        tic = time.perf_counter()
        current = self.frontier.get()
        while not current.state.isGoal(self.goal):
            self.explored.add(current.tobytes())
            for node in current.expand(self.h):
                if node.tobytes() not in self.explored:
                    self.frontier.put(node) 
            if self.frontier.empty():
                raise GameError(Exception("game has no solution"))
            if check_frontier:
                maxfrontier = max(maxfrontier, self.frontier.size())
            current = self.frontier.get()
        solution = deque()
        while current.action is not None:
            solution.appendleft(current.action)
            current = current.father
        toc = time.perf_counter()
        return solution, toc-tic, maxfrontier


