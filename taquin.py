import numpy as np

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
      self.avail = np.where(self.mat == 0)
      self.path = []
      
    def move_left(self):
        if self.avail[1] == 0: #0 correspond a ligne et 1 a colonne
            raise Exception("cannot move left")
        else: 
            self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]][self.avail[1]-1]
            self.mat[self.avail[0]][self.avail[1]-1] = 0
            
    def move_right(self):
        if self.avail[1] == self.n-1:
            raise Exception("cannot move right")
        else: 
            self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]][self.avail[1]+1]
            self.mat[self.avail[0]][self.avail[1]+1] = 0
        
    """method to slide up, this switches the values in the state matrix between the empty square and the one under it"""
    def move_down(self):
            if self.avail[0] == self.n-1:
                raise Exception("cannot move down")
            else: 
                self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]+1][self.avail[1]]
                self.mat[self.avail[0]+1][self.avail[1]] = 0
                
    def move_up(self):
            if self.avail[0] == 0:
                raise Exception("cannot move up")
            else: 
                self.mat[self.avail[0]][self.avail[1]] = self.mat[self.avail[0]-1][self.avail[1]]
                self.mat[self.avail[0]-1][self.avail[1]] = 0
                
    def showmat(self):
        # Afficher la grille du taquin dans la console.
        for ligne in self.mat:
            for col in ligne:
                if col == 0:
                    print(" ", end="\t")
                else:
                    print(col, end="\t")
            print()
            
taq = Taquin(8, True)
taq.showmat()