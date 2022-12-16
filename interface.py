from tkinter import *
from taquin import Taquin
import numpy as np

taquin = Taquin(15,True)
    

FONT=('Ubuntu', 27, 'bold')
master=Tk()
cnv=Canvas(master, width=400, height=400, bg='gray70')
cnv.pack(side="left")

btn=Button(text="Mix", command=mix(4))
btn.pack()

for i in range(4):
    for j in range(4):
        x, y=100*j, 100*i
        A, B, C=(x, y), (x+100, y+100), (x+50, y+50)
        rect=cnv.create_rectangle(A, B, fill="royal blue")
        txt=cnv.create_text(C, text=taquin.mat[i][j], fill="yellow",
                            font=FONT)
        
cnv.delete(rect)
cnv.delete(txt)
master.mainloop()