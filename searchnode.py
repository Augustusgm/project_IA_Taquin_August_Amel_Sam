from taquin import Taquin
from heuristics import heuristic2, heuristic1, no_heuristic
import numpy as np

class SearchNode:
    'this class contains the game, of size n, in the form of a matrice. n is the size of the game, r = True or False generates a shuffled or ordered version of the game'
    
    def __init__(self,taquin : Taquin,father ,nb_action : int ,action : str, h = heuristic2):
        self.state = taquin
        self.father = father
        self.action = action
        self.nb_action = nb_action
        self.val = h(self.state) + self.nb_action
            
        
    #def from_path(self, path):
    #    self.path = path.copy()
    #    self.val = self.h(self.state) + len(self.path)
    
 
    def expand(self, h):
        """method to extand the frontier with an heuristic give us  """
    
        succ = []
        act = ['R','L','D','U']
        for i in range(4):
            try:
                tmp = self.state.clone()
                if act[i] == 'R' :
                    tmp.move_right()
                if act[i] == 'L' :
                    tmp.move_left()
                if act[i] == 'D' :
                    tmp.move_down()
                if act[i] == 'U' :
                    tmp.move_up()
                succ.append(SearchNode(taquin = tmp, father = self,nb_action = self.nb_action+1, action = act[i], h = h ))
            except AssertionError:
                pass
        return succ
    
    def tobytes(self):
        """method to access to the data of searchNode and l'utiliser en general dans le code"""
        return self.state.tobytes()
    

    