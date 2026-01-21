import tkinter as tk, tkinter.ttk as ttk
from tkinter import scrolledtext
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Clasa care creeaza un ScrolledText (caseta de text cu scrollbar) cu o eticheta
class LabeledTextbox(scrolledtext.ScrolledText):
    def __init__(self, master, label_text, label_position, textbox_height, textbox_width, frame_row, frame_column, rowspan, columnspan, **options):

        # Creeaza un frame in care punem label-ul si textbox-ul
        self.frame = tk.Frame(master)

        # Creeaza un label cu textul specificat
        self.label = tk.Label(self.frame, text = label_text)

        # Plaseaza frame-ul in fereastra principala folosind grid
        self.frame.grid(row = frame_row, column = frame_column, rowspan = rowspan, columnspan = columnspan, padx = 10, pady = 10)

        # Creeaza caseta de text cu scrollbar cu dimensiunile dorite
        super().__init__(self.frame, height=textbox_height, width=textbox_width, wrap = "word")

        # Pozitioneaza label-ul fata de textbox, in functie de label_position
        if label_position == 'n':
            self.label.grid(row = 0, column = 0)
            self.grid(row = 1, column = 0)
        if label_position == 's':
            self.label.grid(row = 1, column = 0)
            self.grid(row = 0, column = 0)
        if label_position == 'w':
            self.label.grid(row = 0, column = 0)
            self.grid(row = 0, column = 1)
        if label_position == 'e':
            self.label.grid(row = 0, column = 1)
            self.grid(row = 0, column = 0)

# Clasa care creeaza un Entry cu o eticheta
class LabeledEntry(tk.Entry):
    def __init__(self, master, label_text, label_position, entry_width, frame_row, frame_column):

        # Creeaza un frame in care punem label-ul si entry-ul
        self.frame = tk.Frame(master)

        # Creeaza un label cu textul specificat
        self.label = tk.Label(self.frame, text = label_text)

        # Plaseaza frame-ul in fereastra principala folosind grid
        self.frame.grid(row = frame_row, column = frame_column, padx = 10, pady = 10)

        # Creeaza entry-ul cu setarile dorite
        super().__init__(self.frame, width = entry_width, justify = "center")

        # Pozitioneaza label-ul fata de entry, in functie de label_position
        if label_position == 'n':
            self.label.grid(row = 0, column = 0)
            self.grid(row = 1, column = 0)
        if label_position == 's':
            self.label.grid(row = 1, column = 0)
            self.grid(row = 0, column = 0)
        if label_position == 'w':
            self.label.grid(row = 0, column = 0)
            self.grid(row = 0, column = 1)
        if label_position == 'e':
            self.label.grid(row = 0, column = 1)
            self.grid(row = 0, column = 0)

# Clasa ce implementeaza un combobox cu functie de cautare
class ImprovedComboBox(tb.Combobox):
    def __init__(self, master, **options):

        self.values = options['values']

        self.StringVariable = tk.StringVar(master, self.values[0])

        options['textvariable'] = self.StringVariable
        super().__init__(master, **options)
        self['values'] = self.values

        self.bind('<KeyPress>', self.search)
        self.bind('<KeyRelease>', self.search)

    def search(self, event):
        searchValue = event.widget.get()
        goodValues = []
        if searchValue == '' or searchValue == " ":
            goodValues = self.values
        else:
            goodValues = [name for name in self['values'] if searchValue.lower() in name.lower()]


        self['values'] = goodValues