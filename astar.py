import taquin
import StateSet2 #creer size add
from queue import PriorityQueue
import SearchNode # creer expand 

class Astar :
    def __init__(self, root , explored, frontier):
        self.root = root
        self.explored = StateSet2()
        self.frontier = PriorityQueue()
        self.frontier.put((0,self.root))
        
    def solve(self):
        unsolved = True
        current = self.frontier.get()
        while unsolved:
            print("taille frontiere" + self.frontier.size() + "taille extended" + self.explored.size())
            listSucc = current.expand()
            self.explored.add(current)
            i = 0
            while i < listSucc.size():
                i= i +1
                node = listSucc.get(i)
                if node not in self.frontier:
                    self.frontier.push(node)
        #faire un truc pour trouver le path