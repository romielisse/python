#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

import db

class PreferencesFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent

        # Define string variables for text entry fields
        self.name = tk.StringVar()
        self.language = tk.StringVar()
        self.autoSaveMins = tk.StringVar()

        # Define string variables for validation error fields
        self.nameError = tk.StringVar()
        self.languageError = tk.StringVar()
        self.autoSaveMinsError = tk.StringVar()

        # Read preferences from file and populate entry fields
        try:
            preferences = db.read_preferences()
        except FileNotFoundError:
            preferences = {"name": "",
                           "language": "English",
                           "autosave": 10}
        self.name.set(preferences["name"])
        self.language.set(preferences["language"])
        self.autoSaveMins.set(preferences["autosave"])

        self.initComponents()

    def initComponents(self):
        self.pack()
        
        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Name:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.name).grid(
            column=1, row=0)
        ttk.Label(self, text="", textvariable=self.nameError).grid(
            column=2, row=0, sticky=tk.W)

        ttk.Label(self, text="Language:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.language).grid(
            column=1, row=1)
        ttk.Label(self, text="", textvariable=self.languageError).grid(
            column=2, row=1, sticky=tk.W)

        ttk.Label(self, text="Auto Save Every X Minutes:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.autoSaveMins).grid(
            column=1, row=2)
        ttk.Label(self, text="", textvariable=self.autoSaveMinsError).grid(
            column=2, row=2, sticky=tk.W)

        self.makeButtons()

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Save", command=self.save) \
            .grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Cancel", command=self.cancel) \
            .grid(column=1, row=0)

    def clearMessages(self):
        self.nameError.set("")
        self.languageError.set("")
        self.autoSaveMinsError.set("")

    def save(self):
        valid_data = True
        self.clearMessages()
        
        if self.name.get().strip() == "":
            self.nameError.set("Required.")
            valid_data = False

        if self.language.get().strip() == "":
            self.languageError.set("Required.")
            valid_data = False

        if self.autoSaveMins.get().strip() == "":
            self.autoSaveMinsError.set("Required.")
            valid_data = False

        try:
            mins = int(self.autoSaveMins.get())
        except ValueError:
            self.autoSaveMinsError.set("Must be valid integer.")
            valid_data = False

        if valid_data == False:
            return
        else:
            preferences = {}
            preferences["name"] = self.name.get()
            preferences["language"] = self.language.get()
            preferences["autosave"] = mins
            db.write_preferences(preferences)
            self.parent.destroy()

    def cancel(self):
        self.parent.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Preferences")
    PreferencesFrame(root)
    root.mainloop()
