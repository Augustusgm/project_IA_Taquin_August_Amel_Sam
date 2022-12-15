from taquin import Taquin, InvalidMove
from heuristic1 import Heuristic1
from heuristic2 import Heuristic2
class SearchNode:
    
    def __init__(self,taquin : Taquin,itera : int,father,action, h = Heuristic1()):
        self.nbrAction =itera
        self.h = h
        self.father = father
        self.state = taquin #moveleft ..
        self.action_father = action
        self.value = h.value(self.state) + self.nbrAction
        
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
                succ.append(SearchNode(taquin = tmp, itera = self.nbrAction+1, father = self, action = act[i], h = self.h ))
            except InvalidMove:
                pass
        return succ
    
    def tobytes(self):
        return self.state.tobytes()
    

    