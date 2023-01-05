from taquin import Taquin
from heuristics import heuristic2, heuristic1, no_heuristic
import numpy as np

class SearchNode:
    """
    A class used to represent a Node and expand the frontier 


    Attributes
    ----------
    state : Taquin
        current state
        
    father : Searchnode or None fro root node
        father node
        
    action : str
        the action L or R or D or U applied from father state to get to current state
        
    nb_action : int
        number of actions to get to current node from root node
        
    val : int
        value for the heuristic + nb_action
    

    Methods
    -------
    expand : expand the frontier 
    tobytes : creates hashable instance of the state
    """
    
    def __init__(self,taquin : Taquin,father ,nb_action : int ,action : str, h = heuristic2):
        """
        Parameters
        ----------
        taquin : Taquin
            current state
            
        father : Searchnode or None fro root node
            father node
            
        action : str
            the action L or R or D or U
            
        nb_action : int
            number of actions
            
        h : heuristic
            the heuristic use to find the value
        """
        self.state = taquin
        self.father = father
        self.action = action
        self.nb_action = nb_action
        self.val = h(self.state) + self.nb_action
            
    def expand(self, h):
        """
        method to extand the frontier with an heuristic give us
        
        Parameters
        ----------
        h: the heuristic used
        
        Output
        ------
        list : a list of searchnodes
        """
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
        """creates hashable instance of the state
        
        Returns
        -------
        Bytes: byte representation of state matrix"""
        return self.state.tobytes()
    

    