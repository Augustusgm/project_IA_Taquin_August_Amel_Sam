from taquin import Taquin, GameError
from prQueue import PrQueue
from collections import deque
from searchnode import SearchNode # creer expand , voir pour heuristic, successor, nbr action


class Astar :
    def __init__(self, root : Taquin):
        self.root = SearchNode(root,0,father = None, action =None)
        self.explored = set()
        self.frontier = PrQueue()
        self.frontier.put(self.root)
        
    def solve(self):
        current = self.frontier.get()
        while not current.state.isGoal():
            if current.tobytes() not in self.explored:
                print("taille frontiere ", self.frontier.size(), " taille extended ", len(self.explored))
                listSucc = current.expand()
                for i in listSucc:
                    i.state.showmat()
                    print("\n",i.action_father,"\n")
                self.explored.add(current.tobytes())
                for node in listSucc:
                    self.frontier.put(node) 
            if self.frontier.empty():
                raise GameError(Exception("game has no solution"))
            current = self.frontier.get()
        solution = deque()
        while current != self.root:
            solution.appendleft(current.action_father)
            current = current.father
        return solution


