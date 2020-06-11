in_cm = 0.3937
cm_m  = 100
in_yd = 36
m_yd  = 1.0936
m_km  = 1000
yd_mi = 1760
km_mi = 0.62137


from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

window = ThemedTk(theme="breeze")
tab_control = ttk.Notebook(window)

def length_option_chosen(*args):
    global length_multiplier
    if length_unit1.get() == length_unit2.get():
        length_multiplier = 1
    if length_unit1.get() == 'Inch (in)' and length_unit2.get() == 'Centimetres (cm)':
        length_multiplier = 1/in_cm
    if length_unit1.get() == 'Inch (in)' and length_unit2.get() == 'Yard (yd)':
        length_multiplier = 1/in_yd
    if length_unit1.get() == 'Inch (in)' and length_unit2.get() == 'Metres (m)':
        length_multiplier = 1/(in_cm*cm_m)
    if length_unit1.get() == 'Inch (in)' and length_unit2.get() == 'Miles (mi)':
        length_multiplier = 1/(in_yd*yd_mi) 
    if length_unit1.get() == 'Inch (in)' and length_unit2.get() == 'Kilometres (km)':
        length_multiplier = 1/(in_cm*m_km)
    if length_unit1.get() == 'Centimetres (cm)' and length_unit2.get() == 'Inch (in)':
        length_multiplier = in_cm
    if length_unit1.get() == 'Centimetres (cm)' and length_unit2.get() == 'Yard (yd)':
        length_multiplier = in_cm/in_yd
    if length_unit1.get() == 'Centimetres (cm)' and length_unit2.get() == 'Metres (m)':
        length_multiplier = 1/cm_m
    if length_unit1.get() == 'Centimetres (cm)' and length_unit2.get() == 'Miles (mi)':
        length_multiplier = km_mi*cm_m*m_km
    if length_unit1.get() == 'Centimetres (cm)' and length_unit2.get() == 'Kilometres (km)':
        length_multiplier =  1/(cm_m*m_km)
    if length_unit1.get() == 'Yard (yd)' and length_unit2.get() == 'Inch (in)':
        length_multiplier = in_yd
    if length_unit1.get() == 'Yard (yd)' and length_unit2.get() == 'Centimetres (cm)':
        length_multiplier = 1/(m_yd/cm_m)
    if length_unit1.get() == 'Yard (yd)' and length_unit2.get() == 'Metres (m)':
        length_multiplier = 1/m_yd
    if length_unit1.get() == 'Yard (yd)' and length_unit2.get() == 'Miles (mi)':
        length_multiplier = 1/yd_mi
    if length_unit1.get() == 'Yard (yd)' and length_unit2.get() == 'Kilometres (km)':
        length_multiplier = 1/(m_yd*m_km)
    if length_unit1.get() == 'Metres (m)' and length_unit2.get() == 'Inch (in)':
        length_multiplier =  in_cm*cm_m
    if length_unit1.get() == 'Metres (m)' and length_unit2.get() == 'Centimetres (cm)':
        length_multiplier =  cm_m
    if length_unit1.get() == 'Metres (m)' and length_unit2.get() == 'Yard (yd)':
        length_multiplier = m_yd
    if length_unit1.get() == 'Metres (m)' and length_unit2.get() == 'Miles (mi)':
        length_multiplier = km_mi/m_km
    if length_unit1.get() == 'Metres (m)' and length_unit2.get() == 'Kilometres (km)':
        length_multiplier = 1/m_km
    if length_unit1.get() == 'Miles (mi)' and length_unit2.get() == 'Inch (in)':
        length_multiplier = in_yd*yd_mi
    if length_unit1.get() == 'Miles (mi)' and length_unit2.get() == 'Centimetres (cm)':
        length_multiplier = 1/(km_mi*cm_m*m_km)
    if length_unit1.get() == 'Miles (mi)' and length_unit2.get() == 'Yard (yd)':
        length_multiplier = yd_mi
    if length_unit1.get() == 'Miles (mi)' and length_unit2.get() == 'Metres (m)':
        length_multiplier = 1/(km_mi/m_km)
    if length_unit1.get() == 'Miles (mi)' and length_unit2.get() == 'Kilometres (km)':
        length_multiplier = 1/km_mi
    if length_unit1.get() == 'Kilometres (km)' and length_unit2.get() == 'Inch (in)':
        length_multiplier = in_cm*m_km
    if length_unit1.get() == 'Kilometres (km)' and length_unit2.get() == 'Centimetres (cm)':
        length_multiplier = cm_m*m_km
    if length_unit1.get() == 'Kilometres (km)' and length_unit2.get() == 'Yard (yd)':
        length_multiplier = (m_yd*m_km)
    if length_unit1.get() == 'Kilometres (km)' and length_unit2.get() == 'Metres (m)':
        length_multiplier =  m_km
    if length_unit1.get() == 'Kilometres (km)' and length_unit2.get() == 'Miles (mi)':
        length_multiplier = km_mi

def length_calculate(value):
    value = value.get()
    value = float(value)*length_multiplier
    length_variable2.set(value)


tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Length')

# DROPDOWNS

length_options=['Inch (in)',
                'Centimetres (cm)',
                'Yard (yd)',
                'Metres (m)',
                'Miles (mi)',
                'Kilometres (km)']

length_choices = ttk.Frame(tab2)
length_choices.pack()

length_unit1 = StringVar(length_choices)
length_unit1.trace("w", length_option_chosen)

length_unit2 = StringVar(length_choices)
length_unit2.trace("w", length_option_chosen)

length_choice1 = ttk.OptionMenu(length_choices, length_unit1, length_options[0], *length_options)
length_choice1.config(width=30)
length_choice1.grid(row=1, column=1, padx=5, pady=5)

length_choice2 = ttk.OptionMenu(length_choices, length_unit2, length_options[1], *length_options)
length_choice2.config(width=30)
length_choice2.grid(row=1, column=2, padx=5, pady=5)

# ENTRY WIDGETS

length_entries = ttk.Frame(tab2)
length_entries.pack()

length_variable1 = StringVar()
length_variable2 = StringVar()
length_variable1.trace("w", lambda name, index, mode, sv=length_variable1: length_calculate(length_variable1))
length_variable1.set(1)

length_input1 = ttk.Entry(length_entries, textvariable=length_variable1)
length_input1.grid(row=0, column=1, padx=5, pady=5)
length_input1.config(width=34)

length_input2 = ttk.Entry(length_entries, textvariable=length_variable2)
length_input2.grid(row=0, column=2, padx=5, pady=5)
length_input2.config(state='readonly', width=34)

# BUTTON (unnecessary, but will be nice to have when changing units and not changing the value)
def length_button_wake():
    length_variable1.set(length_variable1.get())

length_button = ttk.Button(tab2, text="Convert", width=69, command=length_button_wake)
length_button.pack(padx=5, pady=5)

def length_swap():
    unit1 = length_unit1.get()
    unit2 = length_unit2.get()
    length_unit1.set(unit2)
    length_unit2.set(unit1)

length_swapper = ttk.Button(tab2, text="Swap Units", width=69, command=length_swap)
length_swapper.pack(padx=5, pady=5)

tab_control.pack(expand=1, fill='both')

window.mainloop()