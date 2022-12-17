from heapdict import heapdict
from taquin import Taquin
from searchnode import SearchNode
from memory_profiler import profile
import sys
class PrQueue:
    
    def __init__(self, root: Taquin, h):
        self._queue = heapdict()
        self._dict = {}
        self.root = root
        self.h = h
        self.i = 1
    
    
    def put(self, node : SearchNode):
        node_key = node.tobytes()
        if (node_key not in self._dict) or (self._queue[node_key]>node.val):
            self._dict[node_key] = node.path
            self._queue[node_key] = node.val
        
        
    def get(self):
        self.i+=1
        if self.i%10000 ==0:
            print('taille dict', sys.getsizeof(self._dict))
        path = self._dict.pop(self._queue.popitem()[0])
        s = SearchNode(taquin = self.root.copy_move_path(path), father = None, action= None, h = self.h, setValue=False)
        s.from_path(path)
        return s
    
    def empty(self):
        return not bool(self._dict)
    
    def size(self):
        return len(self._dict)