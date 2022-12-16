from heapdict import heapdict
from searchnode import SearchNode
from memory_profiler import profile
import sys
class PrQueue:
    
    def __init__(self):
        self._queue = heapdict()
        self._dict = {}
        self.i = 0
    
    
    def put(self, node : SearchNode):
        node_key = node.to_char()
        self.i+=1
        if (node_key not in self._dict) or (self._queue[node_key]>node.val):
            self._dict[node_key] = node
            self._queue[node_key] = node.val
        if self.i%1000 ==0:
            print(sys.getsizeof(self._queue))
            print()
        
    def get(self):
        return self._dict.pop(self._queue.popitem()[0])
        
    def empty(self):
        return not bool(self._dict)
    
    def size(self):
        return len(self._dict)