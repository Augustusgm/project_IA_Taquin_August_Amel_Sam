import heapdict
from searchnode import SearchNode

class PrQueue:
    
    def __init__(self):
        self._queue = heapdict()
        self._dict = {}
        
    def put(self, node : SearchNode):
        if (node.state.mat not in self._dict) or (self._queue[node.state.mat]>node.value):
            self._dict[node.state.mat] = node
            self._queue[node.state.mat] = node.value
        
    def get(self):
        return self._dict[self._queue.popitem()[0]]
        
    def empty(self):
        return self._queue.isEmpty()