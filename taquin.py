import numpy as np

class Taquin:
    'this class contains the game, of size n, in the form of a matrice. n is the size of the game, r = "random" generates a shuffled version of the game and any other returns a ordered version. '
    
    def __init__(self, n, r = 'random'):
      self.n = n
      seq = np.arange(1, self.n**2 -1).append(None)
      if r == 'random':
          np.random.Generator.shuffle(seq)
      self.mat = np.matrix(seq,(self.n,self.n))
      self.avail = np.where(self.mat == None)
      
    def move_right(self):
        if self.avail[0] == 0:
            raise Exception("cannot move right")
        else: 
            self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]][self.avail[1]-1]
            self.mat[self.avail[0]][self.avail[1]-1] = None
            
    def move_left(self):
        if self.avail[0] == self.n:
            raise Exception("cannot move left")
        else: 
            self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]][self.avail[1]+1]
            self.mat[self.avail[0]][self.avail[1]+1] = None
        
"""method to slide up, this switches the values in the state matrix between the empty square and the one under it"""
def move_up(self):
        if self.avail[1] == self.n:
            raise Exception("cannot move up")
        else: 
            self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]+1][self.avail[1]]
            self.mat[self.avail[0]+1][self.avail[1]] = None
            
def move_down(self):
        if self.avail[1] == self.n:
            raise Exception("cannot move down")
        else: 
            self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]-1][self.avail[1]]
            self.mat[self.avail[0]-1][self.avail[1]] = None