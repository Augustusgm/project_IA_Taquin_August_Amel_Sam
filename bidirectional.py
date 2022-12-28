from taquin import Taquin, GameError
from prQueue import PrQueue
from collections import deque
from searchnode import SearchNode
from heuristics import heuristic2, heuristic1, no_heuristic, heuristic2_b
import time

class Bidirectional :
    def __init__(self, root : Taquin,heuristic_f, heuristic_b):
        self.root = SearchNode(root,father = None, action =None,nb_action = 0, h = heuristic_f)
        self.f_h = heuristic_f
        self.b_h = no_heuristic#heuristic_b
        self.f_explored = set()
        self.b_explored = set()
        self.f_frontier = PrQueue()
        self.b_frontier = PrQueue()
        self.goal = SearchNode(Taquin(root.n(),False),father = None, action =None,nb_action = 0, h = no_heuristic)
     
    def solve(self):
        tic = time.perf_counter()
        #current = self.frontier.get()
        current_f = self.root
        current_b = self.goal
        i = -1
        while not (current_f.tobytes() in self.b_explored) or not (current_b.tobytes() in self.f_explored):
            i+=1
            if i%100000 == 0:
                print("taille frontiere forward ", self.f_frontier.size(), " taille extended forward", len(self.f_explored))
                print("taille frontiere backwards ", self.b_frontier.size(), " taille extended backwards", len(self.b_explored))
                current_f.state.showmat()
                toc = time.perf_counter()
                print(f"You have been looking for the solution for {toc - tic:0.4f} seconds")
            self.f_explored.add(current_f.tobytes())
            self.b_explored.add(current_b.tobytes())            
            for node in current_f.expand(self.f_h):
                if node.tobytes() not in self.f_explored:
                    self.f_frontier.put(node) 
            for node in current_b.expand(self.b_h):
                if node.tobytes() not in self.b_explored:
                    self.b_frontier.put(node)
            if self.b_frontier.empty() or self.f_frontier.empty():
                raise GameError(Exception("game has no solution"))
            current_f = self.f_frontier.get()
            current_b = self.b_frontier.get()
        solution = deque()
        while current_f.action is not None:
            solution.appendleft(current_f.action)
            current_f = current_f.father
        while current_b.action is not None:
            solution.append(current_b.action)
            current_b = current_b.father
        toc = time.perf_counter()
        print(f"Found solution in {toc - tic:0.4f} seconds")
        return solution


