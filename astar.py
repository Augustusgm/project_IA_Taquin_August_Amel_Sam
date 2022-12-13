import taquin
import StateSet2 #faire une hash map plutot peut etre
from queue import PriorityQueue
import SearchNode # creer expand , voir pour heuristic, successor, nbr action


class Astar :
    def __init__(self, root , explored, frontier):
        self.root = SearchNode()
        self.explored = StateSet2()
        self.frontier = PriorityQueue()
        self.frontier.put((0,self.root))
        self
        
    def solve(self):
        unsolved = True
        current = self.frontier.get()
        while unsolved:
            if not(current in explored):
                print("taille frontiere" + self.frontier.size() + "taille extended" + self.explored.size())
                listSucc = current.expand()
                self.explored.add(current)
                for i in range(len(listSucc)):
                    node = listSucc.get(i) #avec une priority queue get donne celui avec le cost plus petit
                    #si dans la frtoniere voir si c'est plus petite valeur, on remplace ou ajoute jsp
                    self.frontier.push(node)  
            current = self.frontier.pop() 
            if current.state == current.state.goal():
                unsolved = False
                    
        #faire un truc pour trouver le path
        #faire un truc pour bouger vraiment dans l'interface