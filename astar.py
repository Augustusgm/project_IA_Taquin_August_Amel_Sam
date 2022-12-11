import taquin
import StateSet2 #creer size add
import PriorityQueueState #creer size contains get
import SearchNode # creer expand 

class Astar :
    def __init__(self, root , explored, frontier):
        self.root = taquin.avail()
        self.explored = StateSet2()
        self.frontier = PriorityQueueState()
        self.frontier.push(self.root)
        
    def solve(self):
        current = self.frontier.pop()
        while:
            print("taille frontiere" + self.frontier.size() + "taille extended" + self.explored.size())
            listSucc = current.expand()
            self.explored.add(current)
            i = 0
            for i<listSucc.size():
                i= i +1
                node = listSucc.get(i)
                if (!self.frontier.contains(node)):
                    self.frontier.push(node)
        #faire un truc pour trouver le path