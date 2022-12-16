import numpy as np
import copy

class Taquin:
    'this class contains the game, of size n, in the form of a matrice. n is the size of the game, r = True or False generates a shuffled or ordered version of the game'
    
    def __init__(self, n : int, r : bool):
      self.game_number = n
      if np.sqrt(n + 1) % 1 != 0:
          raise ValueError('n given cannot create a game')
      self.n = int(np.sqrt(n + 1))
      seq = np.append(np.arange(1, self.n**2),[0])
      if r:
          rng = np.random.default_rng()
          rng.shuffle(seq)
      self.mat = np.reshape(seq,(self.n,self.n))
      self.avail = [self.n-1,self.n-1]
      if r:
          self.avail = list(np.argwhere(self.mat == 0)[0])
    
    def goal(self):
        """method which returns the goal state (this is to avoid storing unnecessary data) """
        seq = np.append(np.arange(1, self.n**2),[0])
        return np.reshape(seq,(self.n,self.n))
        
    def clone(self):
        newTaq = Taquin(self.game_number,False)
        #newTaq.mat = copy.deepcopy(self.mat)
        newTaq.mat = self.mat.copy()
        newTaq.avail = self.avail.copy()
        return newTaq
    
    """method to slide empty square left"""  
    def move_left(self):
        assert self.avail[1] != 0, "cannot move left"
        self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]][self.avail[1]-1] 
        self.mat[self.avail[0]][self.avail[1]-1] = 0
        self.avail[1]-=1
    
    """method to slide empty square right"""          
    def move_right(self):
        assert self.avail[1] != self.n-1, "cannot move right"
        self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]][self.avail[1]+1] 
        self.mat[self.avail[0]][self.avail[1]+1] = 0
        self.avail[1]+=1
        
    """method to slide empty square down, this switches the values in the state matrix between the empty square and the one under it"""
    def move_down(self):
            assert self.avail[0] != self.n-1, "cannot move down"
            self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]+1][self.avail[1]]
            self.mat[self.avail[0]+1][self.avail[1]] = 0
            self.avail[0]+=1

    """method to slide empty square up"""                  
    def move_up(self):
            assert self.avail[0] != 0, "cannot move up"
            self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]-1][self.avail[1]] 
            self.mat[self.avail[0]-1][self.avail[1]] = 0
            self.avail[0]-=1
                
    def showmat(self):
        # Afficher la grille du taquin dans la console.
        for ligne in self.mat:
            for col in ligne:
                if col == 0:
                    print(" ", end="\t")
                else:
                    print(col, end="\t")
            print()
            
    def tobytes(self):
        return self.mat.tobytes()
    
    def isGoal(self):
        return np.all(self.mat == self.goal())
            

class GameError(Exception):
    pass
