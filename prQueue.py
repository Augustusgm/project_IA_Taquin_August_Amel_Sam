from heapdict import heapdict
from taquin import Taquin
from searchnode import SearchNode
from memory_profiler import profile
from heuristics import heuristic2, heuristic1, no_heuristic

class PrQueue:
    
    def __init__(self):#, root: Taquin, h = heuristic2):
        self._queue = heapdict()
        self._dict = {}
        #self.root = root
        #self.h = h
    
    
    def put(self, node : SearchNode):
        node_key = node.tobytes()
        if (node_key not in self._dict) or (self._queue[node_key]>node.val):
            self._dict[node_key] = node#.path
            self._queue[node_key] = node.val
        
    def get(self):
        return self._dict.pop(self._queue.popitem()[0])#s
    
    def empty(self):
        return not bool(self._dict)
    
    def size(self):
        return len(self._dict)