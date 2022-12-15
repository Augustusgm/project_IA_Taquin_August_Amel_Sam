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
        while current.state != current.state.goal():
            if current.state.mat not in self.explored:
                print("taille frontiere" + self.frontier.size() + "taille extended" + self.explored.size())
                listSucc = current.expand()
                self.explored.add(current.state.mat)
                for i in range(len(listSucc)):
                    node = listSucc[i]
                    self.frontier.put(node) 
            if self.frontier.empty():
                raise GameError(Exception("game has no solution"))
            current = self.frontier.get()
        solution = deque()
        while current != self.root:
            solution.appendleft(current.actionFather)
            current = current.father
        return solution


