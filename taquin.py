import numpy as np
import random

class Taquin:
    'this class contains the game, of size n, in the form of a matrice. n is the size of the game, r = True or False generates a shuffled or ordered version of the game'
    
    def __init__(self, n : int, random : bool, solvable : int = 0):
      seq = np.append(np.arange(1, n**2),[0])
      if random and solvable == 0:
          rng = np.random.default_rng()
          rng.shuffle(seq)
      self.mat = np.reshape(seq,(n,n))
      self.avail = [n-1,n-1]
      if random:
          self.avail = list(np.argwhere(self.mat == 0)[0])
          if solvable:
              self.mix_up(solvable)
    
    def n(self):
        """function to avoid storing useless information on the size of the game"""
        return self.mat.shape[0]
    
    def goal(self):
        """method which returns the goal state (this is to avoid storing unnecessary data) """
        seq = np.append(np.arange(1, self.n()**2),[0])
        return np.reshape(seq,(self.n(),self.n()))
    
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
        """method to copy a game configuration, it returns a new game with the same state array"""
        newTaq = Taquin(self.n(),False)
        newTaq.mat = self.mat.copy()
        newTaq.avail = self.avail.copy()
        return newTaq
    
    """def copy_move_path(self , path):
        newTaq = Taquin(self.n(),False)
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
        return newTaq"""
      
    def move_left(self):
        """method to slide empty square left"""
        assert self.avail[1] != 0, "cannot move left"
        self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]][self.avail[1]-1] 
        self.mat[self.avail[0]][self.avail[1]-1] = 0
        self.avail[1]-=1
    
             
    def move_right(self):
        """method to slide empty square right""" 
        assert self.avail[1] != self.n()-1, "cannot move right"
        self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]][self.avail[1]+1] 
        self.mat[self.avail[0]][self.avail[1]+1] = 0
        self.avail[1]+=1
        
    def move_down(self):
            """method to slide empty square down, this switches the values in the state matrix between the empty square and the one under it"""
            assert self.avail[0] != self.n()-1, "cannot move down"
            self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]+1][self.avail[1]]
            self.mat[self.avail[0]+1][self.avail[1]] = 0
            self.avail[0]+=1

    def move_up(self):    
            """method to slide empty square up"""                  
            assert self.avail[0] != 0, "cannot move up"
            self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]-1][self.avail[1]] 
            self.mat[self.avail[0]-1][self.avail[1]] = 0
            self.avail[0]-=1
                
    def showmat(self):
        """prints the game state in the terminal"""
        for ligne in self.mat:
            for col in ligne:
                if col == 0:
                    print(" ", end="\t")
                else:
                    print(col, end="\t")
            print()
            
    def tobytes(self):
        """returns the state of the game in byte form to have a hashable representation of a state"""
        return self.mat.tobytes()
    
    def isGoal(self, goal):
        """method, returns boolean stating if the game has reached the goal state"""
        return np.all(self.mat == goal)
    
    
    def from_file(self,file_name):
        """ method wich read a taquin from a file """
        with open(file_name,"r") as fichier:
            global taquin
            size=0
            for line in fichier : #car length marche pas
                size=size +1
            taquin = Taquin(size,False)
            with open("fichier.TXT","r") as fichier2: #car deja fait un for line in fichier 
                i=0
                for line in fichier2 :
                    data = line.split()
                    for j in range(size):
                        self.mat[i][j]= int(data[j])
                    i = i+1
            self.avail=list(np.argwhere(taquin.mat == 0)[0])

            

class GameError(Exception):
    pass
