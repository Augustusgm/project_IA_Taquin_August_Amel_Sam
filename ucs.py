import taquin
from priorityQueue import PrQueue
from collections import deque
from searchnode import SearchNode
from no_heuristic import No_heuristic

class UCS:
    def __init__(self, root , explored, frontier, h = No_heuristic()):
        self.h = h
        self.root = SearchNode(root,0,father = None, action =None)
        self.explored = set()
        self.frontier = PrQueue() #ordonnée seuelemnt par le cost donc nbrAction
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