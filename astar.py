from taquin import Taquin, GameError
from prQueue import PrQueue
from collections import deque
from searchnode import SearchNode 
import time

class Astar :
    """
    Creates object which solves a game of given initial state with astar (or UCS)
    
    Attributes
    ----------
    root : Taquin
        the initial state
    h :
        the chosen heuristic among the functions in heuristics.py file
    explored : set
        set containing the explored states
    frontier : prQueue
        states yet to explore
    goal:
        the goal state
        
    Method
    ------
    solve : solves the game and gives path. 
    """
    def __init__(self, root : Taquin,heuristic):
        """
        Parameters
        ----------
        root : Taquin 
            the initial state of the game.
                
        heuristic: 
            the chosen heuristic

        """
        
        self.root = SearchNode(root,father = None, action =None,nb_action = 0, h = heuristic)
        self.h = heuristic
        self.explored = set()
        self.frontier = PrQueue()
        self.frontier.put(self.root)
        self.goal = self.root.state.goal()
     
    def solve(self, check_frontier = False):
        """
        method to solve the given game
        
        Parameters
        ----------
        check_frontier : bool, optional
            should the output include the maximum size of the frontier (default is False)

        Output
        ------
        tuple containing (path, computation time, frontier max size)
        
        Raises
        ------
        GameError
            If no path exists to reach the goal state
        """
        maxfrontier = 1
        tic = time.perf_counter()
        current = self.frontier.get()
        while not current.state.isGoal(self.goal):
            self.explored.add(current.tobytes())
            for node in current.expand(self.h):
                if node.tobytes() not in self.explored:
                    self.frontier.put(node) 
            if self.frontier.empty():
                raise GameError(Exception("game has no solution"))
            if check_frontier:
                maxfrontier = max(maxfrontier, self.frontier.size())
            current = self.frontier.get()
        solution = deque()
        while current.action is not None:
            solution.appendleft(current.action)
            current = current.father
        toc = time.perf_counter()
        return solution, toc-tic, maxfrontier


