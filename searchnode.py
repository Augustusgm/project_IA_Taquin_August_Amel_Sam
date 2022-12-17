from taquin import Taquin
from heuristics import heuristic2, heuristic1, no_heuristic
import numpy as np

class SearchNode:
    def __init__(self,taquin : Taquin,father ,nb_action : int ,action, h = heuristic2):
        self.state = taquin
        #self.path = []
        self.father = father
        self.action = action
        self.nb_action = nb_action
        #if father is not None:
        #    self.path= father.path.copy()
        #    self.path.append(action)
        #self.val = 0
        #if setValue:
        self.val = h(self.state) + self.nb_action#len(self.path)
            
        
    #def from_path(self, path):
    #    self.path = path.copy()
    #    self.val = self.h(self.state) + len(self.path)
        
    def expand(self, h):
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
        return self.state.tobytes()
    

    