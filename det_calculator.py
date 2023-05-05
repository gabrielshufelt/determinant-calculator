"""
@author: Gabriel Shufelt
Calculator - Determinant of Matrices 
"""

from tkinter import *
from matrix2 import *
from matrix3 import *
from PIL import Image, ImageTk

class Main_window:
    def __init__(self):
        
        # Main Window
        self.window = Tk()
        self.window.title("Determinant calculator")
        self.window.config(background = "#47476b")

        self.choice = IntVar()
        
        # Main Window Labels
        self.title_label = Label(self.window, 
                            text="Determinant Calculator!",
                            bg = "#3d3d5c", 
                            fg = "#ffffff",
                            font = ("Consolas", 20, 'bold'))   
        self.title_label.grid(row=0,columnspan=2)
        self.select_size_label = Label(self.window, 
                                  text="Please select a matrix size",
                                  bg = "#3d3d5c", 
                                  fg = "#ffffff",
                                  font = ("Consolas", 20, 'bold'))
        self.select_size_label.grid(row=1,columnspan=2)
        self.demo_label = Label(self.window, 
                                  text="How does it work?",
                                  bg = "#3d3d5c", 
                                  fg = "#ffffff",
                                  font = ("Consolas", 20, 'bold'))
        self.demo_label.grid(row=5,columnspan=2)
        self.text_label = Label(self.window, 
                                  text="This program can calculate the determinant\n of matrices of sizes 2x2 or 3x3. Matrix \ncalculations are a fundamental part of linear\n algebra and are used by computers all the time.",
                                  bg = "#3d3d5c", 
                                  fg = "#ffffff",
                                  font = ("Consolas", 16))
        self.text_label.grid(row=6,columnspan=2)
        self.explanation_label = Label(self.window,
                                       text = "Shown above are the formulas used to calculate\n the determinants of 2x2 and 3x3 matrices respectively.",
                                       bg = "#3d3d5c",
                                       fg = "#ffffff",
                                       font = ("Consolas", 12))
        self.explanation_label.grid(row=9, columnspan = 2)
        
        # IMAGES
        self.image_open = Image.open("det2.png")          
        self.det2_img = ImageTk.PhotoImage(self.image_open)    
        self.det2_label = Label(self.window, image = self.det2_img)  
        self.det2_label.grid(row=7, columnspan=2)
        
        self.image_open1 = Image.open("det3.png")          
        self.det3_img = ImageTk.PhotoImage(self.image_open1)    
        self.det3_label = Label(self.window, image = self.det3_img)  
        self.det3_label.grid(row=8, columnspan=2)

        # Main Window Radio Buttons
        self.matrix2_button = Radiobutton(self.window,
                                     text = "2x2",
                                     font = ("Consolas", 20, 'bold'),
                                     var = self.choice,
                                     value = 0)
        self.matrix2_button.grid(row=2,column=0)

        self.matrix3_button = Radiobutton(self.window,
                                     text = "3x3",
                                     font = ("Consolas", 20, 'bold'),
                                     var = self.choice,
                                     value = 1)
        self.matrix3_button.grid(row=2,column=1)
        
        self.choice.set(2)          # setting initial selection to none
        
        # Main Window Submit Button
        self.submit_button = Button(self.window,
                                    text = "Submit",
                                    bg = "#3d3d5c", 
                                    fg = "#ffffff",
                                    font = ("Consolas", 20, 'bold'),
                                    command = self.submit)
        self.submit_button.grid(row=3,columnspan=2)
        
        self.window.mainloop()
        
    def submit(self):
        if self.choice.get() == 0:
            matrix2 = Matrix2()
        elif self.choice.get() == 1:
            matrix3 = Matrix3()
        else:
            print("Select a matrix size.")
        
main_window = Main_window()