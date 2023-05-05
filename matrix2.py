"""
@author: Gabriel Shufelt
"""
from tkinter import *

class Matrix2:
    def __init__(self):
        self.window = Tk()
        
        # Labels
        self.label_2x2 = Label(self.window, text = "2x2 Matrix Determinant Calculator")
        self.label_2x2.grid(row=0,columnspan=2)
    
        # Entries
        self.a = Entry(self.window)
        self.a.grid(row=1,column=0)
        self.b = Entry(self.window)
        self.b.grid(row=1,column=1)
        self.c = Entry(self.window)
        self.c.grid(row=2,column=0)
        self.d = Entry(self.window)
        self.d.grid(row=2,column=1)
        
        # Buttons
        self.submit_button = Button(self.window, text = "Calculate", command = self.calculate)
        self.submit_button.grid(row=3,columnspan=2)
        
        self.window.mainloop()
        
    def calculate(self):
        self.a1 = self.a.get()
        self.b1 = self.b.get()
        self.c1 = self.c.get()
        self.d1 = self.d.get()
        self.entries = [self.a1,self.b1,self.c1,self.d1]
        self.count = 0
        
        ''' I used a count system to detect weird entries so code cannot crush
        if the user's entry can be turned into an integer, count will not change
        if the user's entry cannot be turned into an int, count += 1 
        if count > 0, will tell user invalid input
        I used try/except method because I did not know how to specify error with if/elif'''
        
        for e in self.entries:
            try:
                int(e)
            except ValueError:
                self.count +=1
        
        if self.count == 0:
            self.determinant = int(self.a1)*int(self.d1)-int(self.b1)*int(self.c1)
            print(f"Determinant of 2x2 matrix = {self.determinant}")
        else:
            print("Inputs have to be integers. Ex: 100, -2, 0")
        