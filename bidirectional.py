from taquin import Taquin, GameError
from prQueue import PrQueue
from collections import deque
from searchnode import SearchNode
from heuristics import heuristic2, heuristic1, no_heuristic
import time

class Bidirectional :
    def __init__(self, root : Taquin):
        self.root = SearchNode(root,father = None, action =None,nb_action = 0, h = no_heuristic)
        self.f_explored = set()
        self.b_explored = set()
        self.f_frontier = PrQueue()
        self.b_frontier = PrQueue()
        self.goal = SearchNode(Taquin(root.n(),False),father = None, action =None,nb_action = 0, h = no_heuristic)
        self.f_frontier.put(self.root)
        self.b_frontier.put(self.goal)
        
    def solve(self, check_frontier = False):
        maxfrontier = 2
        tic = time.perf_counter()
        current_f = self.f_frontier.get()
        current_b = self.b_frontier.get()
        doWhile = True
        if current_f.tobytes() ==  current_b.tobytes():
            doWhile = False
        while doWhile:
            self.f_explored.add(current_f.tobytes())
            self.b_explored.add(current_b.tobytes())    
            for node in current_f.expand(no_heuristic):
                if node.tobytes() not in self.f_explored:
                    self.f_frontier.put(node)                        
            for node in current_b.expand(no_heuristic):
                if node.tobytes() not in self.b_explored:
                    self.b_frontier.put(node)
            if self.b_frontier.empty() or self.f_frontier.empty():
                raise GameError(Exception("game has no solution"))
            if check_frontier:
                maxfrontier = max(maxfrontier, self.f_frontier.size()+self.b_frontier.size())
            if current_f in self.b_frontier:
                current_b = self.b_frontier.get_item(current_f)
                break
            if current_b in self.f_frontier:
                current_f = self.f_frontier.get_item(current_b)
                break 
            current_f = self.f_frontier.get()
            if current_f in self.b_frontier:
                current_b = self.b_frontier.get_item(current_f)
                break
            current_b = self.b_frontier.get()
            if current_b in self.f_frontier:
                current_f = self.f_frontier.get_item(current_b)
                break 
        while not(self.b_frontier.empty() or self.f_frontier.empty()):
            next_f = self.f_frontier.get()
            if next_f.val>current_f.val:
                break
            if next_f in self.b_frontier:
                next_b = self.b_frontier.get_item(next_f)
                if (next_f.val + next_b.val)<(current_f.val + current_b.val):
                    current_f =next_f
                    current_b = next_b
        solution = deque()
        while current_f.action is not None:
            solution.appendleft(current_f.action)
            current_f = current_f.father
        reverse_action = {'U':'D','D':'U','L':'R','R':'L'}
        while current_b.action is not None:
            solution.append(reverse_action[current_b.action])
            current_b = current_b.father
        toc = time.perf_counter()
        return solution, toc-tic, maxfrontier
