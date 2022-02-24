#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox
import math

from triangle import RightTriangle

class RightTriangleFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.message = ""

        # Define string variables for text entry fields
        self.sideA = tk.StringVar()
        self.sideB = tk.StringVar()
        self.sideC = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        self.pack()

        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Side A:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=40, textvariable=self.sideA).grid(
            column=1, row=0)

        ttk.Label(self, text="Side B:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=40, textvariable=self.sideB).grid(
            column=1, row=1)

        ttk.Label(self, text="Side C:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=40, textvariable=self.sideC,
                  state="readonly").grid(column=1, row=2)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate) \
            .grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Exit", command=self.parent.destroy) \
            .grid(column=1, row=0)

    def get_int(self, value, fieldName):
        try:
            return int(value)
        except ValueError:
            self.message += f"{fieldName} must be a valid integer.\n"

    def get_side(self, value, fieldName):
        value = self.get_int(value, fieldName)
        # get_int() returns None if validation fails - in that case,
        # don't need to do any further validation
        if value is None or value > 0:  
            return value
        else:
            self.message += f"{fieldName} must be greater than zero.\n"

    def calculate(self):
        self.message = "" # clear any previous error message
        
        # get sides A and B from user
        triangle = RightTriangle()
        triangle.sideA = self.get_side(self.sideA.get(), "Side A")
        triangle.sideB = self.get_side(self.sideB.get(), "Side B")
           
        # if input OK, display side C - otherwise, notify user
        if self.message == "": # no errors
            sideC = round(triangle.sideC, 3)
            self.sideC.set(sideC)
        else:
            messagebox.showerror("Error", self.message)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Right Triangle Calculator")
    RightTriangleFrame(root)
    root.mainloop()
