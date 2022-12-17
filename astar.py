from taquin import Taquin, GameError
from prQueue import PrQueue
from collections import deque
from searchnode import SearchNode 
from memory_profiler import profile
import sys


class Astar :
    def __init__(self, root : Taquin,heuristic):
        self.root = SearchNode(root,father = None, action =None, h = heuristic)
        self.explored = set()
        self.frontier = PrQueue(root , heuristic)
        #self.frontier.put(self.root)
        self.goal = self.root.state.goal()
    
    @profile    
    def solve(self):
        #current = self.frontier.get()
        current = self.root
        i = -1
        while not current.state.isGoal(self.goal):
            i+=1
            if i%10000 == 0:
                print("taille frontiere ", self.frontier.size(), " taille extended ", len(self.explored))
                print('taille explored', sys.getsizeof(self.explored))
                current.state.showmat()
            listSucc = []
            listSucc = current.expand()
            self.explored.add(current.tobytes())
            for node in listSucc:
                if node.tobytes() not in self.explored:
                    self.frontier.put(node) 
            if self.frontier.empty():
                raise GameError(Exception("game has no solution"))
            current = self.frontier.get()
        solution = current.path
        return solution


