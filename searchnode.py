from taquin import Taquin
from heuristic1 import Heuristic1
from heuristic2 import Heuristic2
from no_heuristic import No_heuristic
import numpy as np

class SearchNode:
    def __init__(self,taquin : Taquin,father ,action, h = Heuristic2(), setValue = True):
        self.state = taquin
        self.path = []
        self.h = h
        if father is not None:
            self.path= father.path.copy()
            self.path.append(action)
        self.val = 0
        if setValue:
            self.val = h.value(self.state) + len(self.path)
            
        
    def from_path(self, path):
        self.path = path.copy()
        self.val = self.h.value(self.state) + len(self.path)
        
    def expand(self):
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
                succ.append(SearchNode(taquin = tmp, father = self, action = act[i], h = self.h ))
            except AssertionError:
                pass
        return succ
    
    def tobytes(self):
        return self.state.tobytes()
    

    