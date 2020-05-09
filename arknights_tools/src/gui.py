"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import tkinter as tk
from tkinter import Canvas, Label

class Application(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        
        self.pack()
        self.make_gui()
        
        
    def make_gui(self):    
        print("making gui")
        w = Label(self, text="Hello, world!")
        w.pack()
        
root = tk.Tk()
canvas = Canvas(root, width=400, height=400)
app = Application(root)
root.pack_propagate(0) #Prevents window shrinkage

root.mainloop()