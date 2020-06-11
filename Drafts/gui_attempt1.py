from tkinter import *
# import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

window = ThemedTk(theme="breeze")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Mass')



tab2 = ttk.Frame(tab_control)

tab3 = ttk.Frame(tab_control)

tab4 = ttk.Frame(tab_control)

tab5 = ttk.Frame(tab_control)

tab6 = ttk.Frame(tab_control)

tab_control.add(tab2, text='Length')

tab_control.add(tab3, text='Speed')

tab_control.add(tab4, text='Temperature')

tab_control.add(tab5, text='Currency')

tab_control.add(tab6, text='Date')

# lbl1 = Label(tab1, text= 'label1')

# lbl1.grid(column=0, row=0)

m_buttons = ttk.Frame(tab1)
m_buttons.pack()

m_value1 = tk.StringVar()
m_value2 = tk.StringVar()

m_options =['Kilograms (kg)', 
            'Pounds (lbs)', 
            'Stone (st)']

def yo(*args):
    print('yo')

m_b1 = ttk.OptionMenu(m_buttons, m_value1, m_options[1], *m_options)
m_value1.trace("w", yo)
m_b1.config(width=16)
m_b1.grid(row=1, column=1, padx=5, pady=5)

m_b2 = ttk.OptionMenu(m_buttons, m_value2, m_options[2], *m_options)
m_b2.config(width=16)
m_b2.grid(row=1, column=2, padx=5, pady=5)

m_entries = ttk.Frame(tab1)
m_entries.pack()

m_v1 = tk.StringVar()
m_v1.trace("w", lambda name, index, mode, sv=m_v1: calculate(m_v1))
m_e1 = ttk.Entry(m_entries, textvariable=m_v1)
m_e1.grid(row=0, column=1, padx=5, pady=5)

m_v2 = tk.StringVar()
m_e2 = ttk.Entry(m_entries, textvariable=m_v2)
m_e2.grid(row=0, column=2, padx=5, pady=5)
m_e2.config(state='readonly')



def calculate(value):
    pass
#     m_v2.set(float(sv.get())*3) 

tab_control.pack(expand=1, fill='both')

window.mainloop()