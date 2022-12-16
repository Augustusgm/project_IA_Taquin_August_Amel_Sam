from random import randrange
from tkinter import *
import numpy as np
import random
from taquin import Taquin
from astar import Astar 
from heuristic2 import Heuristic2



def clic(event):
    global i_empty, j_empty, bravo
    if bravo:
        return
    i=event.y//100 #coordonnée des clics
    j=event.x//100
    nro=taquin.mat[i][j]
    tile, txt=items[nro] 
    if j+1 ==j_empty and i==i_empty: #if elif pour voir si on peut deplacer a droite a gauche en haut en bas 
        cnv.move(tile, 100, 0)
        cnv.move(txt, 100, 0)
    elif j-1 ==j_empty and i==i_empty:
        cnv.move(tile, -100, 0)
        cnv.move(txt, -100, 0)
    elif i+1 ==i_empty and j==j_empty:
        cnv.move(tile, 0, 100)
        cnv.move(txt, 0, 100)
    elif i-1 ==i_empty and j==j_empty:
        cnv.move(tile, 0, -100)
        cnv.move(txt, 0, -100)
    else:
        return
    taquin.mat[i][j] , taquin.mat[i_empty][j_empty] = (taquin.mat[i_empty][j_empty] , taquin.mat[i][j])
    i_empty=i
    j_empty=j
    if (taquin.mat==taquin.goal()).all():
        lbl.configure(text="Bravo !")
        bravo=True


def mix():
    print("appel a mix")
    global i_empty, j_empty, items, taquin, bravo
    cnv.delete("all")
    items=[None]
    taquin.mix_up(300) 
    i_empty, j_empty= taquin.avail
    empty=i_empty, j_empty
    items=[None for i in range(taquin.n **2 )]

    for i in range(taquin.n):
        for j in range(taquin.n):
            x, y=100*j, 100*i
            A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
            rect=cnv.create_rectangle(A, B, fill="mediumturquoise")
            txt=cnv.create_text(C, text=taquin.mat[i][j], fill="deeppink",
                                font=FONT)
            items[taquin.mat[i][j]]=(rect, txt) # items[12] : un tuple de la forme (rect, txt) où rect : id rectangle de la tuile 12 txt l’id du texte 12 ici
    rect, txt=items[0]
    cnv.delete(txt)
    cnv.delete(rect)
    lbl.configure(text="")
    bravo=False
    
def choisir_taquin():
    global taquin 
    num = int(taille.get())
    taquin = Taquin(num-1,True)
    mix()
    
def choix_astar_h2(): #se servir de la classe solve dans le futur 
    x=Astar(root = taquin, heuristic = Heuristic2()).solve()
    print('solution: ',x)
    
FONT=('Ubuntu', 27, 'bold')
master=Tk()

libelle = Label(master, text='Entrez la taille de votre taquin:')
libelle.pack()

taille = Entry(master)
taille.pack(pady=10)
bouton_soumission = Button(master, text='Enter', command=choisir_taquin, padx=15, pady=5)
bouton_soumission.pack(padx=10, pady=(0, 10))

taquin = Taquin(15,True)

cnv=Canvas(master, width=taquin.n*100, height=taquin.n*100, bg='gray70')
cnv.pack(side='left')

lbl=Label(text="      ", font=('Ubuntu', 25, 'bold'),
          justify=CENTER, width=7)
lbl.pack(side="left")


btn=Button(text="Mélanger", command=mix)
btn.pack()

b1 = Button (text = "solve with Astar with h1")
b1.pack()
b2 = Button (text = "solve with Astar with h2", command=choix_astar_h2)
b2.pack()
b3 = Button (text = "solve with UCS")
b3.pack()
b4 = Button (text = "solve with IDA")
b4.pack()
b5 = Button (text = "solve with biderectionnal")
b5.pack()


cnv.bind("<Button-1>",clic)



    
master.mainloop()