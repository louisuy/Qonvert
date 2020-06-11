aed_usd = 3.67
aed_gbp = 4.65
usd_gbp = 1.27


from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

window = ThemedTk(theme="breeze")
tab_control = ttk.Notebook(window)

def currency_option_chosen(*args):
    global currency_multiplier
    if currency_unit1.get() == currency_unit2.get():
        currency_multiplier = 1
    if currency_unit1.get() == 'United Arab Emirates Dirham (AED)' and currency_unit2.get() == 'United States Dollar (USD)':
        currency_multiplier = 1/aed_usd
    if currency_unit1.get() == 'United States Dollar (USD)' and currency_unit2.get() == 'United Arab Emirates Dirham (AED)':
        currency_multiplier = aed_usd
    if currency_unit1.get() == 'Pound Sterling (GBP)' and currency_unit2.get() == 'United States Dollar (USD)':
        currency_multiplier = usd_gbp
    if currency_unit1.get() == 'United States Dollar (USD)' and currency_unit2.get() == 'Pound Sterling (GBP)':
        currency_multiplier = 1/usd_gbp
    if currency_unit1.get() == 'United Arab Emirates Dirham (AED)' and currency_unit2.get() == 'Pound Sterling (GBP)':
        currency_multiplier = 1/aed_gbp
    if currency_unit1.get() == 'Pound Sterling (GBP)' and currency_unit2.get() == 'United Arab Emirates Dirham (AED)':
        currency_multiplier = aed_gbp

def currency_calculate(value):
    value = value.get()
    value = float(value)*currency_multiplier
    currency_variable2.set(value)


tab5 = ttk.Frame(tab_control)
tab_control.add(tab5, text='Speed')

# DROPDOWNS

currency_options = ['United Arab Emirates Dirham (AED)',
                 'United States Dollar (USD)',
                 'Pound Sterling (GBP)']

currency_choices = ttk.Frame(tab5)
currency_choices.pack()

currency_unit1 = StringVar(currency_choices)
currency_unit1.trace("w", currency_option_chosen)

currency_unit2 = StringVar(currency_choices)
currency_unit2.trace("w", currency_option_chosen)

 

currency_choice2 = ttk.OptionMenu(currency_choices, currency_unit2, currency_options[1], *currency_options)
currency_choice2.config(width=30)
currency_choice2.grid(row=1, column=2, padx=5, pady=5)

# ENTRY WIDGETS

currency_entries = ttk.Frame(tab5)
currency_entries.pack()

currency_variable1 = StringVar()
currency_variable2 = StringVar()
currency_variable1.trace("w", lambda name, index, mode, sv=currency_variable1: currency_calculate(currency_variable1))
currency_variable1.set(1)

currency_input1 = ttk.Entry(currency_entries, textvariable=currency_variable1)
currency_input1.grid(row=0, column=1, padx=5, pady=5)
currency_input1.config(width=34)

currency_input2 = ttk.Entry(currency_entries, textvariable=currency_variable2)
currency_input2.grid(row=0, column=2, padx=5, pady=5)
currency_input2.config(state='readonly', width=34)

# BUTTON (unnecessary, but will be nice to have when changing units and not changing the value)
def currency_button_wake():
    currency_variable1.set(currency_variable1.get())

currency_button = ttk.Button(tab5, text="Convert", width=69, command=currency_button_wake)
currency_button.pack(padx=5, pady=5)

def currency_swap():
    unit1 = currency_unit1.get()
    unit2 = currency_unit2.get()
    currency_unit1.set(unit2)
    currency_unit2.set(unit1)

currency_swapper = ttk.Button(tab5, text="Swap Units", width=69, command=currency_swap)
currency_swapper.pack(padx=5, pady=5)

tab_control.pack(expand=1, fill='both')

window.mainloop()