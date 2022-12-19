from heapdict import heapdict
from taquin import Taquin
from searchnode import SearchNode
from memory_profiler import profile
from heuristics import heuristic2, heuristic1, no_heuristic
import sys
from types import ModuleType, FunctionType
from gc import get_referents

# Custom objects know their class.
# Function objects seem to know way too much, including modules.
# Exclude modules as well.


def getsize(obj):
    """sum size of object & members."""
    BLACKLIST = type, ModuleType, FunctionType
    if isinstance(obj, BLACKLIST):
        raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size

import sys
class PrQueue:
    
    def __init__(self):#, root: Taquin, h = heuristic2):
        self._queue = heapdict()
        self._dict = {}
        #self.root = root
        #self.h = h
        self.i = 1
    
    
    def put(self, node : SearchNode):
        node_key = node.tobytes()
        if (node_key not in self._dict) or (self._queue[node_key]>node.val):
            self._dict[node_key] = node#.path
            self._queue[node_key] = node.val
        
        
    def get(self):
        self.i+=1
        if self.i%1000000 ==0:
            print('taille dict', getsize(self._dict))
       # path = self._dict.pop(self._queue.popitem()[0])
       # s = SearchNode(taquin = self.root.copy_move_path(path), father = None, action= None, h = self.h, setValue=False)
        #s.from_path(path)
        return self._dict.pop(self._queue.popitem()[0])#s
    
    def empty(self):
        return not bool(self._dict)
    
    def size(self):
        return len(self._dict)