from tkinter import *
from tkinter import ttk
from Getting_exchange_rates import Start_Communication

class CurrencyTransfer:
    def creating_a_window_from_hryvnia_to_dollars(self):
        new_grn_to_dll = Toplevel()
        new_grn_to_dll.title("converter")
        new_frm = ttk.Frame(new_grn_to_dll, padding=10)
        new_frm.grid()
        result = 0
    
        def output_result():
            try:
                Number_of_hryvnia = float(Entering_numbers.get())
                
                if Number_of_hryvnia < 0:
                    raise(ValueError)
            except:
                ttk.Label(new_frm, text="Вы ввели неверный данные").grid(column=0, row=5)
                
            call = Start_Communication()
            data = call.communication_call()
            result = Number_of_hryvnia / data
            ttk.Label(new_frm, text=round(result, 2)).grid(column=0, row=4)

        ttk.Label(new_frm, text="Перевод из гривен в доллары").grid(column=0, row=0)
        ttk.Label(new_frm, text="Введите какую сумму гривен вы хотите перевести в доллары").grid(column=0, row=1)
        Entering_numbers = ttk.Entry(new_frm)
        Entering_numbers.grid(column=0, row=2)
        ttk.Button(new_frm, text="Получить перевод", command= lambda : output_result()).grid(column=0, row=3)
    
    
        new_grn_to_dll.mainloop()
        
        return Entering_numbers, result
        
    def creating_a_window_from_dollar_to_hryvnia(self):
        new_dll_to_grn = Toplevel()
        new_dll_to_grn.title("converter")
        new_frm = ttk.Frame(new_dll_to_grn, padding=10)
        new_frm.grid()
        result = 0
    
        def output_result():
            try:
                Number_of_hryvnia = float(Entering_numbers.get())
            except:
                ttk.Label(new_frm, text="Вы ввели неверный данные").grid(column=0, row=5)
                
            call = Start_Communication()
            data = call.communication_call()
            result = Number_of_hryvnia * data
            ttk.Label(new_frm, text=round(result, 2)).grid(column=0, row=4)
    
        ttk.Label(new_frm, text="Перевод долларов в гривны").grid(column=0, row=0)
        ttk.Label(new_frm, text="Введите какую сумму долларов вы хотите перевести в гривны").grid(column=0, row=1)
        Entering_numbers = ttk.Entry(new_frm)
        Entering_numbers.grid(column=0, row=2)
        ttk.Button(new_frm, text="Получить перевод", command= lambda : output_result()).grid(column=0, row=3)
    
    
        new_dll_to_grn.mainloop()