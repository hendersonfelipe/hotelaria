from __main__ import*
import sys

try:
    from tkinter import*
except ImportError:
    from tkinter import*

try:
    from tkinter import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

fo1=open("recipt.txt", "r")
list1=fo1.readlines()
del list1[1]
del list1[2]
del list1[3]
del list1[4]
del list1[5]

list1[0]= list1[0][:-1]
list1[1]= list1[1][:-1]
list1[2]= list1[2][:-1]
list1[3]= list1[3][:-1]
list1[4]= list1[4][:-1]


p='''
====================== HOTEL 089 FIVE STARS ======================
=============== AV. PADRE MANOEL PAREDES, CURRAIS-PI ===============
====================== SERVINDO DESDE 2017 ======================
========================= ### 1997 ### =========================
============================================================
     
NOME - %s
ENDEREÇO - %s
Nº TELEFONE - %s
TOTAL DA CONTA R$ %s
Nº DO QUARTO - %s
'''%(list1[0],list1[1],list1[2],list1[4],list1[3])

class recipt:
    def __init__(self):
        
        root=Tk()

        _bgcolor ='#ffffff'
        _fgcolor ='#000000'
        _compcolor ='#ffffff'
        _ana1color ='#ffffff'
        _ana2color ='#ffffff'

        font11 = "-family {Segoe UI} -size 17 -weight bold -slant  "\
            "roman -underline 0 -overstrike 0"
        
        font14 = "-family {Segoe UI} -size 16 -weight bold -slant  "\
            "roman -underline 0 -overstrike 0"
        

        root.geometry("800x600")
        root.title("DK_Python_Hotel - RECIBO")
        root.configure(background="#d9d9d9")
        root.wm_iconbitmap(r"c:\\Tkinter_poo\\ÍCONE\\hotel.ico")

        self.Label1 = Label(root)
        self.Label1.place(relx=0,rely=0,height=800,width=800)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(anchor=N)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text=p)
        self.Label1.configure(wraplength=1000)
        self.Label1.configure(justify=LEFT)
        self.Label1.configure(width=582)


        root.mainloop()

if __name__ == '__main__':
    recipt1=recipt()