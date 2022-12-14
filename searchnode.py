from taquin import Taquin

class SearchNode:
    
    def __init__(self,taquin : Taquin,itera : int,father,action):
        self.nbrAction =itera
        self.father = father
        self.action= action
        self.state = taquin #moveleft ..
        self.actionFather = action
        self.value = SearchNode.h.value(taquin)
        
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
                succ.append(SearchNode(tmp,self.nbrAction+1, self, act[i] ))
            except:
                pass
        return succ
    
    def compare_to(self ,s):
        value = self.nbrActions+self.valH-s.nbrActions-s.valH
        if(value > 0.0001 or value < -0.0001):
            return value
        return self.identifiant - s.identifiant