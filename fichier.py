
from taquin import Taquin

with open("fichier.TXT","r") as fichier:
    i=0
    size = len(fichier)
    taquin = Taquin(size,True)
    for line in fichier :
        size2=len(line.split(","))
        j=0
        for d in line.split(","):
            data = str(d) 
            taquin.mat[i][j]= int(data)
            j=j+1
        i = i+1

taquin.showmat()