from tkinter import *
from taquin import Taquin
import numpy as np


from random import randrange
from tkinter import *

def clic(event):
    global i_empty, j_empty, bravo
    if bravo:
        return
    i=event.y//100
    j=event.x//100
    nro=board[i][j]
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
    board[i][j],board[i_empty][j_empty]=(
        board[i_empty][j_empty],board[i][j])
    i_empty=i
    j_empty=j
    if board==win:
        lbl.configure(text="Bravo !")
        bravo=True

def voisins(n, i, j):
    return [(a,b) for (a, b) in
            [(i, j+1),(i, j-1), (i-1, j), (i+1,j)]
            if a in range(n) and b in range(n)]

def echange(board, empty):
    i, j=empty
    V=voisins(4, i, j)
    ii, jj=V[randrange(len(V))]
    board[ii][jj], board[i][j]=board[i][j],board[ii][jj]
    return ii, jj

def normal(board, empty):
    i_empty, j_empty = empty
    for i in range(i_empty, 4):
        (board[i][j_empty], board[i_empty][j_empty])= (
            board[i_empty][j_empty], board[i][j_empty])
        i_empty=i
    for j in range(j_empty, 4):
        board[i_empty][j], board[i_empty][j_empty]= (
            board[i_empty][j_empty],board[i_empty][j])
        j_empty=j

def melanger(N):
    board=[[4*lin+1+col for col in range(4)]
        for lin in range(4)]

    empty=(3,3)

    for i in range(N):
        empty=echange(board, empty)
    return board

def init(N=5):
    print("appel a mix")
    global i_empty, j_empty, items, board, bravo
    cnv.delete("all")
    items=[None]


    board=melanger(N)
    for i in range(4):
        for j in range(4):
            if board[i][j]==16:
                i_empty, j_empty=i, j

    empty=i_empty, j_empty
    normal(board, empty)
    i_empty, j_empty=3,3
    print(board)
    items=[None for i in range(17)]

    for i in range(4):
        for j in range(4):
            x, y=100*j, 100*i
            A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
            rect=cnv.create_rectangle(A, B, fill="royal blue")
            nro=board[i][j]
            txt=cnv.create_text(C, text=nro, fill="yellow",
                                font=FONT)
            items[nro]=(rect, txt)
    rect, txt=items[16]
    cnv.delete(txt)
    cnv.delete(rect)
    lbl.configure(text="")
    bravo=False

FONT=('Ubuntu', 27, 'bold')
master=Tk()
cnv=Canvas(master, width=400, height=400, bg='gray70')
cnv.pack(side='left')

btn=Button(text="Mélanger", command=init)
btn.pack()

lbl=Label(text="      ", font=('Ubuntu', 25, 'bold'),
          justify=CENTER, width=7)
lbl.pack(side="left")

cnv.bind("<Button-1>",clic)
init()

win=[[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

master.mainloop()