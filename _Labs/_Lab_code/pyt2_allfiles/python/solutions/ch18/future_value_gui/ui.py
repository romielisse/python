#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox
import locale

from business import Investment

class FutureValueFrames(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # Add the FutureValueFrames
        FutureValueFrame(parent).grid(row=0, column=0)
        FutureValueFrame(parent).grid(row=0, column=1)

        # Add the Exit button        
        ttk.Button(parent, text="Exit", command=parent.destroy).grid(
            row=1, column=1, sticky=tk.E, padx=15, pady=10)

class FutureValueFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.investment = Investment()
        self.message = ""
        
        locale.setlocale(locale.LC_ALL, 'en_US')        

        # Define string variables for text entry fields
        self.monthlyInvestment = tk.StringVar()
        self.yearlyInterestRate = tk.StringVar()
        self.years = tk.StringVar()
        self.futureValue = tk.StringVar()

        self.initComponents()

    def initComponents(self):
        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Monthly Investment:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.monthlyInvestment).grid(
            column=1, row=0)

        ttk.Label(self, text="Yearly Interest Rate:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.yearlyInterestRate).grid(
            column=1, row=1)

        ttk.Label(self, text="Years:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.years).grid(
            column=1, row=2)

        ttk.Label(self, text="Future Value:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.futureValue,
                  state="readonly").grid(
            column=1, row=3)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Clear", command=self.clear) \
            .grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Calculate", command=self.calculate) \
            .grid(column=1, row=0)

    def get_float(self, val, fieldName):
        try:
            return float(val)
        except ValueError:
            self.message += f"{fieldName} must be a valid number.\n"

    def get_int(self, val, fieldName):
        try:
            return int(val)
        except ValueError:
            self.message += f"{fieldName} must be a valid whole number.\n"

    def calculate(self):
        self.message = "" # clear any previous error message 
        
        self.investment.monthlyInvestment = self.get_float(
            self.monthlyInvestment.get(), "Monthly investment")
        self.investment.yearlyInterestRate = self.get_float(
            self.yearlyInterestRate.get(), "Yearly interest rate")
        self.investment.years = self.get_int(
            self.years.get(), "Years")

        if self.message == "": # no errors
            self.futureValue.set(locale.currency(
                self.investment.calculateFutureValue(), grouping=True))
        else:
            messagebox.showerror("Error", self.message)

    def clear(self):
        self.monthlyInvestment.set("")
        self.yearlyInterestRate.set("")
        self.years.set("")
        self.futureValue.set("")
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Future Value Calculator")
    FutureValueFrames(root)
    root.mainloop()
