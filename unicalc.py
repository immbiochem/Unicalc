import tkinter as tk
from tkinter import messagebox
import os
import numpy as np

class NumVariable():
    def __init__(self, name, coeff_of_variable):
        self.name = name
        self.coeff_of_variable = coeff_of_variable
        self.text_block = None
    #
    def init_text_block(self, name_of_window,
                        place_x:int, place_y:int,
                        place_width:int, label_txt,
                        label_font:int, label_x:int,
                        label_y:int, label_width:int):
        self.text_blok = ['# - - - - -',
                          f'{self.name}_but = tk.Entry({name_of_window})',
                          f'{self.name}_but.place(x={place_x}, y={place_y}, width={place_width})',
                          f'tk.Label({name_of_window}, text="{label_txt}",'
                          f'\n\tfont=("Arial", {label_font}), bg="white").place(x={label_x}, y={label_y}, width={label_width})',
                          '# - - - - -']

class BinVariable():
    def __init__(self, name, coeff_of_positive_class, name_of_positive_class, name_of_negative_class):
        self.name = name
        self.coeff_of_positive_class = coeff_of_positive_class
        self.name_of_positive_class = name_of_positive_class
        self.name_of_negative_class = name_of_negative_class
        self.text_block = None
    def init_text_block(self, name_of_window,
                        place_x:int, place_y:int,
                        place_width:int, label_txt,
                        label_font:int, label_x:int,
                        label_y:int, label_width:int):
        self.text_blok = ['# - - - - -',
                          f'{self.name}_but = ttk.Combobox(window, values=[{self.name_of_positive_class},{self.name_of_negative_class}], state="readonly")',
                          f'{self.name}_but.place(x={place_x}, y={place_y}, width={place_width})',
                          f'tk.Label({name_of_window}, text="{label_txt}",'
                          f'\n\tfont=("Arial", {label_font}), bg="white").place(x={label_x}, y={label_y}, width={label_width})',
                          '# - - - - -']
