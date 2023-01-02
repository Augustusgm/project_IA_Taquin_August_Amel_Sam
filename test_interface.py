from random import randrange
from tkinter import *
import numpy as np
import random
from taquin import Taquin
from astar import Astar 
from bidirectional import Bidirectional
from heuristics import heuristic2, heuristic1, no_heuristic
from fichier import fichier
import time


def clic(event):
    """method to move the title in the puzzle """
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
    taquin.avail=list(np.argwhere(taquin.mat == 0)[0])
    if (taquin.mat==taquin.goal()).all():
        lbl.configure(text="Bravo !")
        bravo=True


def mix():
    """method to mix the tiles in the puzzle"""
    print("appel a mix")
    global i_empty, j_empty, items, taquin, bravo
    cnv.delete("all")
    items=[None]
    taquin.mix_up(300) 
    taquin.avail=list(np.argwhere(taquin.mat == 0)[0])
    i_empty, j_empty= taquin.avail
    items=[None for i in range(taquin.n() **2 )]
    for i in range(taquin.n()):
        for j in range(taquin.n()):
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
    
def afficher():
    """method to print the tiles in the puzzle"""
    global i_empty, j_empty, items, taquin, bravo
    cnv.delete("all")
    items=[None]
    taquin.avail=list(np.argwhere(taquin.mat == 0)[0])
    i_empty, j_empty= taquin.avail
    items=[None for i in range(taquin.n() **2 )]
    for i in range(taquin.n()):
        for j in range(taquin.n()):
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
    """method to have (recuperer) the size of the taquin chose by the user """
    global taquin 
    num = int(taille.get())
    taquin = Taquin(num,False,100)
    mix()
    
def choix_astar_h2(): #se servir de la classe solve dans le futur 
    """method to launch the algo astar with h2 and print the result """
    tic = time.perf_counter()
    x=Astar(root = taquin, heuristic = heuristic2).solve()
    toc = time.perf_counter()
    z = toc -tic
    Texte.set("Résultat: " + str(x) + " \n Found solution in " + str(z))

def choix_astar_h1(): #se servir de la classe solve dans le futur 
    """method to launch astar with h1 and print the result """
    tic = time.perf_counter()
    x=Astar(root = taquin, heuristic = heuristic1).solve()
    Texte.set("Résultat: " + str(x))
    toc = time.perf_counter()
    z = toc -tic
    Texte.set("Résultat: " + str(x) + " \n Found solution in " + str(z))

def choix_bidirectional():
    tic = time.perf_counter()
    x = Bidirectional(root = taquin).solve()
    Texte.set("Résultat: " + str(x))
    toc = time.perf_counter()
    z = toc -tic
    Texte.set("Résultat: " + str(x) + " \n Found solution in " + str(z))

def choix_ucs():
    """method to launch UCS and print the result """
    tic = time.perf_counter()
    x = Astar(root = taquin, heuristic = no_heuristic).solve()
    Texte.set("Résultat: " + str(x))
    toc = time.perf_counter()
    z = toc -tic
    Texte.set("Résultat: " + str(x) + " \n Found solution in " + str(z))

def choisir_taquin_exactly():
    """method to have (recuperer) a taquin in fichier chose by the user """
    global taquin 
    taquin = fichier()
    afficher()
   
FONT=('Ubuntu', 27, 'bold')
master=Tk()
master.title('Taquin')

libelle = Label(master, text='Entrez la taille de votre taquin: 3, 4, 5 ...')
libelle.pack()

taille = Entry(master)
taille.pack(pady=10)
bouton_soumission = Button(master, text='Enter', command=choisir_taquin, padx=15, pady=5)
bouton_soumission.pack(padx=10, pady=(0, 10))



cnv=Canvas(master, width=800, height=700)
cnv.pack(side='left')

lbl=Label(text="      ", font=('Ubuntu', 25, 'bold'),
          justify=CENTER, width=7)
lbl.pack(side="left")

Texte = StringVar()
LabelResultat = Label(master, textvariable = Texte , bg ="grey")
LabelResultat.pack()

btn=Button(text="Mélanger", command=mix)
btn.pack()

b5 = Button (text = "choose your taquin with fichier", command=choisir_taquin_exactly)
b5.pack()

b1 = Button (text = "solve with Astar with h1", command=choix_astar_h1)
b1.pack()
b2 = Button (text = "solve with Astar with h2", command=choix_astar_h2)
b2.pack()
b3 = Button (text = "solve with UCS", command=choix_ucs)
b3.pack()
b4 = Button (text = "solve with biderectionnal", command=choix_bidirectional)
b4.pack()


cnv.bind("<Button-1>",clic)



    
master.mainloop()