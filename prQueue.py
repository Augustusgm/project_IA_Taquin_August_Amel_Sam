from heapdict import heapdict
from taquin import Taquin
from searchnode import SearchNode
from memory_profiler import profile
from heuristics import heuristic2, heuristic1, no_heuristic

class PrQueue:
    """
    class which gives the priority queues for the search algorithms
    
    Attributes
    ----------
    _queue (heapdict):
        a priority queue storing byte form of states and their priority order
    _dict :
        python dictionary linking byte form of states to the searchnode whith smallest path
        
    Methods
    -------
    put: add new node to the queue
    get: get next node from the queue
    get_item : return node linked to a particular state without removing it from queue
    empty : checks if queue is empty
    size : gives size of the queue
    __contains__: adapts the contain method for this class
    """
    def __init__(self):
        self._queue = heapdict()
        self._dict = {}
    
    def put(self, node : SearchNode):
        """
        add new node to the queue

        Parameters
        ----------
        node (SearchNode):
            the node to add to the queue
        """
        node_key = node.tobytes()
        if (node_key not in self._dict) or (self._queue[node_key]>node.val):
            self._dict[node_key] = node
            self._queue[node_key] = node.val
        
    def get(self):
        """
        get next node from the queue


        Returns
        -------
        Searchnode: 
            returns next node
        """
        return self._dict.pop(self._queue.popitem()[0])
    
    def get_item(self, node):
        """
        get a specific node from the queue without removing it
        
        Parameters
        ----------
        node (Searchnode):
            node to look for in the Queue(looks for one with same state)
        Returns
        -------
        Searchnode: 
            returns node for specific state
        """
        return self._dict[node.tobytes()]
    
    def empty(self):
        """is it empty?

        Returns:
            bool: if True then the Queue is empty
        """
        return not bool(self._dict)
    
    def size(self):
        """
        Returns:
            int: size of the Queue
        """
        return len(self._dict)
    
    def __contains__(self, node):
        """
        Args:
            node (Searchnode): node to compare states with

        Returns:
            bool: if another node is found whith same sate in the Queue
        """
        return node.tobytes() in self._dict