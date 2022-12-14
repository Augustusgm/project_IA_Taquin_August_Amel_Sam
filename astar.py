import taquin
from queue import PriorityQueue
from searchnode import SearchNode # creer expand , voir pour heuristic, successor, nbr action


class Astar :
    def __init__(self, root , explored, frontier):
        self.root = SearchNode(root,0,father = None, action =None)
        self.explored = set()
        self.frontier = PriorityQueue()
        self.frontier.put((0,self.root))
        
    def solve(self):
        unsolved = True
        current = self.frontier.get()
        while unsolved:
            if current.state.mat not in self.explored:
                print("taille frontiere" + self.frontier.size() + "taille extended" + self.explored.size())
                listSucc = current.expand()
                self.explored.add(current.state.mat)
                for i in range(len(listSucc)):
                    node = listSucc[i] #avec une priority queue get donne celui avec le cost plus petit
                    #si dans la frtoniere voir si c'est plus petite valeur, on remplace ou ajoute jsp
                    self.frontier.push(node)  
            current = self.frontier.pop() 
            if current.state == current.state.goal():
                unsolved = False
                    
        #faire un truc pour trouver le path
        #faire un truc pour bouger vraiment dans l'interface