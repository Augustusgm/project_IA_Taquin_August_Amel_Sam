from random import randrange
from tkinter import *
import numpy as np
from taquin import Taquin
from astar import Astar 
from bidirectional import Bidirectional
from heuristics import heuristic2, heuristic1, no_heuristic


def clic(event):
    """method to perceive where we click in the interface.
    Also tests if the goal is reached"""
    global i_empty, j_empty
    i=event.y//100 
    j=event.x//100
    nro=taquin.mat[i][j]
    tile, txt=items[nro] 
    if j+1 ==j_empty and i==i_empty: 
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


def mix():
    """method to mix the tiles in the puzzle. Each clicks generates 100 random moves which mixes up the tiles"""
    print("appel a mix")
    global i_empty, j_empty, items, taquin
    taquin.mix_up(100) 
    afficher()
    
    
def afficher():
    """method to print the tiles of the puzzle"""
    global i_empty, j_empty, items, taquin
    cnv.delete("all")
    items=[None]
    i_empty, j_empty= taquin.avail
    items=[None for i in range(taquin.n() **2 )]
    for i in range(taquin.n()):
        for j in range(taquin.n()):
            x, y=100*j, 100*i
            A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
            rect=cnv.create_rectangle(A, B, fill="mediumturquoise")
            txt=cnv.create_text(C, text=taquin.mat[i][j], fill="deeppink",
                                font=FONT)
            items[taquin.mat[i][j]]=(rect, txt) 
    rect, txt=items[0]
    cnv.delete(txt)
    cnv.delete(rect)
    lbl.configure(text="")
    bravo=False
    

def choose_taquin():
    """method to have get the size of the taquin chosen by the user and test if it is a good size """
    global taquin 
    Texte.set("")
    num = int(size.get())
    if np.sqrt(num + 1) % 1 != 0:
        text.set("this number " + str(num) + " cannot create a game, you can choose another one ")
    else :
        taquin = Taquin(int(np.sqrt(num + 1)),False)
        afficher()
        text.set("")
    
    
def choice_astar_h2(): 
    """method to launch the algo astar with h2 and print the result """
    x, t, fr =Astar(root = taquin, heuristic = heuristic2).solve()
    Texte.set("Résultat: " + str(list(x)) + "\n size " + str(len(x)) + " \n Found solution in " + str(t))

def choice_astar_h1(): 
    """method to launch astar with h1 and print the result """
    x, t , r=Astar(root = taquin, heuristic = heuristic1).solve()
    Texte.set("Résultat: " + str(list(x)) + "\n size " + str(len(x)) + " \n Found solution in " + str(t))

def choice_bidirectional():
    """method to launch bidirectionnal algo and print the result """
    x, t ,fr = Bidirectional(root = taquin).solve()
    Texte.set("Résultat: " + str(list(x)) + "\n size " + str(len(x)) + " \n Found solution in " + str(t))

def choice_ucs():
    """method to launch UCS and print the result """
    x, t , fr= Astar(root = taquin, heuristic = no_heuristic).solve()
    Texte.set("Résultat: " + str(list(x)) + "\n size " + str(len(x)) + " \n Found solution in " + str(t))

def choose_taquin_exactly():
    """method to get a taquin from the file fichier.txt """
    global taquin 
    taquin = Taquin(2,False)
    from_file("fichier.txt")
    afficher()
    
    
def from_file(file_name):
        """ method which reads a taquin from a file
        file_name : the file which is read"""
        global taquin
        with open(file_name,"r") as fichier:
            size=0
            for line in fichier :
                size=size +1
            if taquin.n()!=size:
                taquin = Taquin(size,False)
        with open(file_name,"r") as fichier2: #car deja fait un for line in fichier 
            i=0
            for line in fichier2 :
                data = line.split()
                for j in range(len(data)):
                    taquin.mat[i][j] = int(data[j])
                i = i+1
        taquin.avail=list(np.argwhere(taquin.mat == 0)[0])
   
FONT=('Ubuntu', 27, 'bold')
master=Tk()
master.title('Taquin')

libelle = Label(master, text='Enter the size of the taquin : 3, 8, 15, 24 ...')
libelle.pack()

size = Entry(master)
size.pack(pady=10)

bouton_soumission = Button(master, text='Enter', command=choose_taquin, padx=15, pady=5)
bouton_soumission.pack(padx=10, pady=(0, 10))

cnv=Canvas(master, width=800, height=700)
cnv.pack(side='left')

lbl=Label(text="      ", font=('Ubuntu', 25, 'bold'),
          justify=CENTER, width=7)
lbl.pack(side="left")

text = StringVar()
label = Label(master,textvariable = text, bg ="red")
label.pack()

Texte = StringVar()
LabelResultat = Label(master, textvariable = Texte , bg ="pink")
LabelResultat.pack()


btn=Button(text="Mix (100 random moves)", command=mix)
btn.pack()

b5 = Button (text = "choose your taquin with file : fichier.txt", command=choose_taquin_exactly)
b5.pack()

b1 = Button (text = "solve with Astar with h1", command=choice_astar_h1)
b1.pack()

b2 = Button (text = "solve with Astar with h2", command=choice_astar_h2)
b2.pack()

b3 = Button (text = "solve with UCS", command=choice_ucs)
b3.pack()

b4 = Button (text = "solve with biderectionnal", command=choice_bidirectional)
b4.pack()

cnv.bind("<Button-1>",clic)
    
master.mainloop()