"""
@author: Gabriel Shufelt
"""
from tkinter import *

class Matrix3:
    def __init__(self):
        self.window = Tk()

        # Labels
        self.label_3x3 = Label(self.window, text = "3x3 Matrix Determinant Calculator")
        self.label_3x3.grid(row=0,columnspan=3)

        # Entries
        self.a = Entry(self.window)
        self.a.grid(row=1,column=0)
        self.b = Entry(self.window)
        self.b.grid(row=1,column=1)
        self.c = Entry(self.window)
        self.c.grid(row=1,column=2)
        self.d = Entry(self.window)
        self.d.grid(row=2,column=0)
        self.e = Entry(self.window)
        self.e.grid(row=2,column=1)
        self.f = Entry(self.window)
        self.f.grid(row=2,column=2)
        self.g = Entry(self.window)
        self.g.grid(row=3,column=0)
        self.h = Entry(self.window)
        self.h.grid(row=3,column=1)
        self.i = Entry(self.window)
        self.i.grid(row=3,column=2)

        # Buttons
        self.submit_button = Button(self.window, text = "Calculate", command = self.calculate)
        self.submit_button.grid(row=4,columnspan=3)
        
        self.window.mainloop()      
        
    def calculate(self):
        self.a1 = self.a.get()
        self.b1 = self.b.get()
        self.c1 = self.c.get()
        self.a2 = self.d.get()
        self.b2 = self.e.get()
        self.c2 = self.f.get()
        self.a3 = self.g.get()
        self.b3 = self.h.get()
        self.c3 = self.i.get()
        self.entries = [self.a1,self.b1,self.c1,self.a2,self.b2,self.c2,self.a3,self.b3,self.c3]
        self.count = 0
        
        for e in self.entries:
            try:
                int(e)
            except ValueError:
                self.count +=1
                
        if self.count == 0:
            # long formula to calculate determinant
            self.determinant = int(self.a1)*(int(self.b2)*int(self.c3)-int(self.b3)*int(self.c2))-int(self.b1)*(int(self.a2)*int(self.c3)-int(self.a3)*int(self.c2))+int(self.c1)*(int(self.a2)*int(self.b3)-int(self.a3)*int(self.b2))
            print(f"Determinant of 3x3 matrix = {self.determinant}")
        else:
            print("Invalid inputs!")
        

