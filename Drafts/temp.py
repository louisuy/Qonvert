FC_multiplier = 1.8000
FC_addend = 32.00
KC_addend = 273.15


from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

window = ThemedTk(theme="breeze")
# window.geometry('350x210')
tab_control = ttk.Notebook(window)

def temp_option_chosen(*args):
    global mode
    if temp_unit1.get() == temp_unit2.get():
        mode = 0
    if temp_unit1.get() == "Fahrenheit (" u"\N{DEGREE SIGN}" "F)" and temp_unit2.get() == "Celsius (" u"\N{DEGREE SIGN}" "C)":
        mode = 1
    if temp_unit1.get() == "Celsius (" u"\N{DEGREE SIGN}" "C)" and temp_unit2.get() == "Fahrenheit (" u"\N{DEGREE SIGN}" "F)":
        mode = 2
    if temp_unit1.get() == "Kelvin (K)" and temp_unit2.get() == "Celsius (" u"\N{DEGREE SIGN}" "C)":
        mode = 3
    if temp_unit1.get() == "Celsius (" u"\N{DEGREE SIGN}" "C)" and temp_unit2.get() == "Kelvin (K)":
        mode = 4
    if temp_unit1.get() == "Kelvin (K)" and temp_unit2.get() == "Fahrenheit (" u"\N{DEGREE SIGN}" "F)":
        mode = 5
    if temp_unit1.get() == "Fahrenheit (" u"\N{DEGREE SIGN}" "F)" and temp_unit2.get() == "Kelvin (K)":
        mode = 6


def temp_calculate(value):
    try:
        value = float(value.get())
        if mode == 0:
            value = value*1
        if mode == 1:
            value = (value-FC_addend)/FC_multiplier
        if mode == 2:
            value = (value*FC_multiplier) + FC_addend
        if mode == 3:
            value = value - KC_addend
        if mode == 4:
            value = value + KC_addend
        if mode == 5:
            value = ((value - KC_addend)*FC_multiplier) + FC_addend
        if mode == 6:
            value = ((value - FC_addend)/FC_multiplier) + KC_addend
        temp_variable2.set(value)
    except ValueError:
        pass


tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text='Temperature')

# DROPDOWNS

temp_options = ["Fahrenheit (" u"\N{DEGREE SIGN}" "F)",
                "Celsius (" u"\N{DEGREE SIGN}" "C)",
                "Kelvin (K)"]

temp_choices = ttk.Frame(tab4)
temp_choices.pack()

temp_unit1 = StringVar(temp_choices)
temp_unit1.trace("w", temp_option_chosen)

temp_unit2 = StringVar(temp_choices)
temp_unit2.trace("w", temp_option_chosen)

temp_choice1 = ttk.OptionMenu(temp_choices, temp_unit1, temp_options[1], *temp_options)
temp_choice1.config(width=30)
temp_choice1.grid(row=1, column=1, padx=5, pady=5)

temp_choice2 = ttk.OptionMenu(temp_choices, temp_unit2, temp_options[0], *temp_options)
temp_choice2.config(width=30)
temp_choice2.grid(row=1, column=2, padx=5, pady=5)

# ENTRY WIDGETS

temp_entries = ttk.Frame(tab4)
temp_entries.pack()

temp_variable1 = StringVar()
temp_variable2 = StringVar()
temp_variable1.trace("w", lambda name, index, mode, sv=temp_variable1: temp_calculate(temp_variable1))
temp_variable1.set(35)

temp_input1 = ttk.Entry(temp_entries, textvariable=temp_variable1)
temp_input1.grid(row=0, column=1, padx=5, pady=5)
temp_input1.config(width=34)

temp_input2 = ttk.Entry(temp_entries, textvariable=temp_variable2)
temp_input2.grid(row=0, column=2, padx=5, pady=5)
temp_input2.config(state='readonly', width=34)

# BUTTON (unnecessary, but will be nice to have when changing units and not changing the value)
def temp_button_wake():
    temp_variable1.set(temp_variable1.get())

temp_button = ttk.Button(tab4, text="Convert", width=69, command=temp_button_wake)
temp_button.pack(padx=5, pady=5)

def temp_swap():
    unit1 = temp_unit1.get()
    unit2 = temp_unit2.get()
    temp_unit1.set(unit2)
    temp_unit2.set(unit1)

temp_swapper = ttk.Button(tab4, text="Swap Units", width=69, command=temp_swap)
temp_swapper.pack(padx=5, pady=5)

tab_control.pack(expand=1, fill='both')

window.mainloop()