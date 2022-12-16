from taquin import Taquin, GameError
from prQueue import PrQueue
from collections import deque
from searchnode import SearchNode 


class Astar :
    def __init__(self, root : Taquin,heuristic):
        self.root = SearchNode(root,father = None, action =None, h = heuristic)
        self.explored = set()
        self.frontier = PrQueue()
        self.frontier.put(self.root)
        
    def solve(self):
        current = self.frontier.get()
        i = 1
        while not current.state.isGoal():
            if current.tobytes() not in self.explored:
                i+=1
                if i%1000 == 0:
                    print("taille frontiere ", self.frontier.size(), " taille extended ", len(self.explored))
                listSucc = current.expand()
                self.explored.add(current.tobytes())
                for node in listSucc:
                    if node.tobytes() not in self.explored:
                        self.frontier.put(node) 
            if self.frontier.empty():
                raise GameError(Exception("game has no solution"))
            current = self.frontier.get()
        #solution = deque()
        #while current != self.root:
        #    solution.appendleft(current.action_father)
        #    current = current.father
        solution = current.path
        return solution


