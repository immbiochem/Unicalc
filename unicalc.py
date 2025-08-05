import tkinter as tk
from tkinter import messagebox
import os
import numpy as np

class NumVariable():
    def __init__(self, name):
        self.type = 'NUM'
        self.name = name
        self.init_var = False
        self.text_block = False

    def init_numvariable(self, coeff_of_variable):
        self.coeff_of_variable = coeff_of_variable
        self.init_var = True

    def init_text_block(self, name_of_window,
                        place_x:int, place_y:int,
                        place_width:int, label_txt,
                        label_font:int, label_x:int,
                        label_y:int, label_width:int):
        if self.init_var:
            self.text_blok = ['# - - - - -',
                              f'{self.name}_but = tk.Entry({name_of_window})',
                              f'{self.name}_but.place(x={place_x}, y={place_y}, width={place_width})',
                              f'tk.Label({name_of_window}, text="{label_txt}",'
                              f'\n\tfont=("Arial", {label_font}), bg="white").place(x={label_x}, y={label_y}, width={label_width})',
                              '# - - - - -']
            self.text_block = True
        else:
            return

class BinVariable():
    def __init__(self, name):
        self.type = 'BIN'
        self.name = name
        self.init_var = False
        self.text_block = False

    def init_binvariable(self, coeff_of_positive_class, name_of_positive_class, name_of_negative_class):
        self.coeff_of_positive_class = coeff_of_positive_class
        self.name_of_positive_class = name_of_positive_class
        self.name_of_negative_class = name_of_negative_class
        self.init_var = True

    def init_text_block(self, name_of_window,
                        place_x:int, place_y:int,
                        place_width:int, label_txt,
                        label_font:int, label_x:int,
                        label_y:int, label_width:int):
        if self.init_var:
            self.text_blok = ['# - - - - -',
                              f'{self.name}_but = ttk.Combobox(window, values=[{self.name_of_positive_class},{self.name_of_negative_class}], state="readonly")',
                              f'{self.name}_but.place(x={place_x}, y={place_y}, width={place_width})',
                              f'tk.Label({name_of_window}, text="{label_txt}",'
                              f'\n\tfont=("Arial", {label_font}), bg="white").place(x={label_x}, y={label_y}, width={label_width})',
                              '# - - - - -']
            self.text_block = True
        else:
            return

class Creator():
    def __init__(self):
        self.name_of_prog = None
        self.num_of_binvars = None
        self.num_of_numvars = None
        self.num_of_vars = None
        self._box = dict()
        self.text_block_of_prog = None

    def init_creator(self, name_of_prog, num_of_binvars:int, num_of_numvars:int):
        self.name_of_prog = name_of_prog
        self.num_of_binvars = num_of_binvars
        self.num_of_numvars = num_of_numvars
        self.num_of_vars = num_of_binvars + num_of_numvars
        self.text_block_of_prog = ['import tkinter as tk\nfrom tkinter import messagebox\nimport os\nimport numpy as np',
                                   'window = tk.Tk()\nwindow.resizable(width=False, height=False)',
                                   f'window.title({name_of_prog})\nwindow.geometry("800x700")\nwindow["bg"] = "gainsboro"',
                                   f'task_to_prog = tk.Label(window, text="{name_of_prog}", font=("Arial", 14), fg="black", bg="white")',
                                   'task_to_prog.place(x=58, y=45, width=700)']

    def create_vars(self):
        for i in range(self.num_of_binvars):
            self._box[f'x_{i}'] = BinVariable(f'x_{i}')

        for i in range(self.num_of_numvars):
            self._box[f'x_{self.num_of_binvars+i}'] = NumVariable(f'x_{self.num_of_binvars+i}')

    def init_vars(self, key_of_var, coeff,
                  name_of_positive_class='Да',
                  name_of_negative_class='Нет'):
        if self._box[key_of_var].type == 'BIN':
            self._box[key_of_var].init_binvariable(coeff,
                                                   name_of_positive_class,
                                                   name_of_negative_class)
        else:
            self._box[key_of_var].init_numvariable(coeff)

class Decorator():
    def __init__(self):
        self.creator = None
    #
    def start_work(self, creator):
        self.craetor = creator
        #
        window = tk.Tk()
        #
        window.resizable(width=False, height=False)
        window.title('UNICALC')
        #
        window.geometry('1000x580')
        #
        window['bg'] = 'gainsboro'
        #
        task_to_prog = tk.Label(window, text='UNICALC',
                                font=('Arial', 20), fg='black', bg='white')
        task_to_prog.place(x=60, y=25, width=676)
        #
        window.mainloop()
