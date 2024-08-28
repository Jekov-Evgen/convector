from tkinter import *
from tkinter import ttk
from Translation_functions import CurrencyTransfer

class Creation():
    def creating_a_window(self):
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        root.title("converter")
        Calling_translation_functions = CurrencyTransfer()

        ttk.Label(frm, text="Приветсвую в конвертере валют").grid(column=0, row=0)
        ttk.Button(frm, text="Из гривен в доллары", command=lambda : Calling_translation_functions.creating_a_window_from_hryvnia_to_dollars()).grid(column=0, row=1)
        ttk.Button(frm, text="Из долларов в гривны", command=lambda : Calling_translation_functions.creating_a_window_from_dollar_to_hryvnia()).grid(column=0, row=2)
        ttk.Button(frm, text="Выход", command=root.destroy).grid(column=0, row=3)


        root.mainloop()