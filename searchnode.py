import taquin

class SearchNode:
    
    def __init__(self,taquin,iter,father,action):
        self.nbrAction =iter
        self.father = father
        self.action= action
        self.state = taquin #moveleft ..
        self.actionFather = action
        self.value = SearchNode.h.value(taquin)
        
    def expand():
        succ = []
        for i in range(4):
            tmp = state.clone()
            if i == 1 :
                tmp.move_right()
            elif i == 2 :
                tmp.move_left()
            elif i == 3 :
                tmp.move_down()
            elif i == 4 :
                tmp.move_up()
            succ.append(SearchNode(tmp,self.nbrAction+1, self, i ))
        return succ
    
        
        
        