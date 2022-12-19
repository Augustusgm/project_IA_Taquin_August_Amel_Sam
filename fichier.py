
from taquin import Taquin

with open("fichier.TXT","r") as fichier:
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
                taquin.mat[i][j]= int(data[j])
            i = i+1


taquin.showmat()
