import taquin

class SearchNode:
    
    def __init__(self,father,action):
        self.nbrAction =+1
        self.father = father
        self.action= action
        self.state = father.action #moveleft ..
        
        
        