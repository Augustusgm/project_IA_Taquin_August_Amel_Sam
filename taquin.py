import numpy as np
import random

class Taquin:
    'this class contains the game, of size n, in the form of a matrice. n is the size of the game, r = True or False generates a shuffled or ordered version of the game'
    
    def __init__(self, n : int, random : bool, solvable : int = 0):
      self.game_number = n
      if np.sqrt(n + 1) % 1 != 0:
          raise ValueError('n given cannot create a game')
      self.n = int(np.sqrt(n + 1))
      seq = np.append(np.arange(1, self.n**2),[0])
      if random and solvable == 0:
          rng = np.random.default_rng()
          rng.shuffle(seq)
      self.mat = np.reshape(seq,(self.n,self.n))
      self.avail = [self.n-1,self.n-1]
      if random:
          self.avail = list(np.argwhere(self.mat == 0)[0])
          if solvable:
              self.mix_up(solvable)
    
    def goal(self):
        """method which returns the goal state (this is to avoid storing unnecessary data) """
        seq = np.append(np.arange(1, self.n**2),[0])
        return np.reshape(seq,(self.n,self.n))
    
    def mix_up(self, n : int):
        """generate n movements, if we start from a goal state then the returned game is solvable."""
        act = ['R','L','D','U']
        for _ in range(n):
            try:
                i=random.randint(0, 3)
                if act[i] == 'R' :
                    self.move_right()
                if act[i] == 'L' :
                    self.move_left()
                if act[i] == 'D' :
                    self.move_down()
                if act[i] == 'U' :
                    self.move_up()
            except AssertionError:
                pass
                
   
    def clone(self):
        newTaq = Taquin(self.game_number,False)
        newTaq.mat = self.mat.copy()
        newTaq.avail = self.avail.copy()
        return newTaq
    
    def copy_move_path(self , path):
        newTaq = Taquin(self.game_number,False)
        newTaq.mat = self.mat.copy()
        newTaq.avail = self.avail.copy()
        for i in path:
            if i == 'R' :
                newTaq.move_right()
            if i == 'L' :
                newTaq.move_left()
            if i == 'D' :
                newTaq.move_down()
            if i == 'U' :
                newTaq.move_up()
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
    
    def isGoal(self, goal):
        return np.all(self.mat == goal)
            

class GameError(Exception):
    pass
