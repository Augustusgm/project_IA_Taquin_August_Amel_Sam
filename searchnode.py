from taquin import Taquin
from heuristic1 import Heuristic1
from heuristic2 import Heuristic2
class SearchNode:
    
    def __init__(self,taquin : Taquin,itera : int,father,action, h = Heuristic1()):
        self.nbrAction =itera
        self.h = h
        self.father = father
        self.action= action
        self.state = taquin #moveleft ..
        self.actionFather = action
        self.value = h.value(self.state) + self.nbrAction
        
    def expand(self):
        succ = []
        act = ['R','L','D','U']
        for i in range(4):
            try:
                tmp = self.state.clone()
                if act[i] == 'R' :
                    tmp.move_right()
                elif act[i] == 'L' :
                    tmp.move_left()
                elif act[i] == 'D' :
                    tmp.move_down()
                elif act[i] == 'U' :
                    tmp.move_up()
                succ.append(SearchNode(tmp, self.nbrAction+1, self, act[i], self.h ))
            except:
                pass
        return succ
    