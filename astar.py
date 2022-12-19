from taquin import Taquin, GameError
from prQueue import PrQueue
from collections import deque
from searchnode import SearchNode 
from memory_profiler import profile
import sys
import time


import sys
from types import ModuleType, FunctionType
from gc import get_referents

# Custom objects know their class.
# Function objects seem to know way too much, including modules.
# Exclude modules as well.


def getsize(obj):
    """sum size of object & members."""
    BLACKLIST = type, ModuleType, FunctionType
    if isinstance(obj, BLACKLIST):
        raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size
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
                print('taille explored', getsize(self.explored))
                print('taille frontier', getsize(self.frontier))
                current.state.showmat()
                toc = time.perf_counter()
                print(f"solving with astar took {toc - tic:0.4f} seconds")
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
        return solution


