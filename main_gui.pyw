kg_lb = 2.2046228
st_lb = 14
st_kg = 6.3502927
mph_kph = 1.609344
kn_mph  = 1.1507795
kn_kph  = 1.852
aed_usd = 3.67
aed_gbp = 4.65
usd_gbp = 1.27
FC_multiplier = 1.8000
FC_addend = 32.00
KC_addend = 273.15
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
from tkcalendar import Calendar, DateEntry
import math

window = ThemedTk(theme="breeze")
window.geometry('565x240')
window.iconbitmap('qonvert.ico')
window.title("Qonvert")
tab_control = ttk.Notebook(window)

#--------------------------------------------------MASS--------------------------------------------------

def mass_option_chosen(*args):
    global mass_multiplier
    if mass_unit1.get() == mass_unit2.get():
        mass_multiplier = 1
    if mass_unit1.get() == 'Kilograms (kg)' and mass_unit2.get() == 'Pounds (lbs)':
        mass_multiplier = kg_lb
    if mass_unit1.get() == 'Pounds (lbs)' and mass_unit2.get() == 'Kilograms (kg)':
        mass_multiplier = 1/kg_lb
    if mass_unit1.get() == 'Stone (st)' and mass_unit2.get() == 'Pounds (lbs)':
        mass_multiplier = st_lb
    if mass_unit1.get() == 'Pounds (lbs)' and mass_unit2.get() == 'Stone (st)':
        mass_multiplier = 1/st_lb
    if mass_unit1.get() == 'Kilograms (kg)' and mass_unit2.get() == 'Stone (st)':
        mass_multiplier = 1/st_kg
    if mass_unit1.get() == 'Stone (st)' and mass_unit2.get() == 'Kilograms (kg)':
        mass_multiplier = st_kg

def mass_calculate(value):
    value = value.get()
    value = float(value)*mass_multiplier
    mass_variable2.set(value)


tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Mass')
ttk.Label(tab1, text='', font=('Segoe', '15')).pack()

# DROPDOWNS

mass_options = ['Kilograms (kg)', 
                'Pounds (lbs)', 
                'Stone (st)']

mass_choices = ttk.Frame(tab1)
mass_choices.pack()

mass_unit1 = StringVar(mass_choices)
mass_unit1.trace("w", mass_option_chosen)

mass_unit2 = StringVar(mass_choices)
mass_unit2.trace("w", mass_option_chosen)

mass_choice1 = ttk.OptionMenu(mass_choices, mass_unit1, mass_options[0], *mass_options)
mass_choice1.config(width=30)
mass_choice1.grid(row=1, column=1, padx=5, pady=5)

mass_choice2 = ttk.OptionMenu(mass_choices, mass_unit2, mass_options[1], *mass_options)
mass_choice2.config(width=30)
mass_choice2.grid(row=1, column=2, padx=5, pady=5)

# ENTRY WIDGETS

mass_entries = ttk.Frame(tab1)
mass_entries.pack()

mass_variable1 = StringVar()
mass_variable2 = StringVar()
mass_variable1.trace("w", lambda name, index, mode, sv=mass_variable1: mass_calculate(mass_variable1))
mass_variable1.set(1)

mass_input1 = ttk.Entry(mass_entries, textvariable=mass_variable1)
mass_input1.grid(row=0, column=1, padx=5, pady=5)
mass_input1.config(width=34)

mass_input2 = ttk.Entry(mass_entries, textvariable=mass_variable2)
mass_input2.grid(row=0, column=2, padx=5, pady=5)
mass_input2.config(state='readonly', width=34)

# BUTTON (unnecessary, but will be nice to have when changing units and not changing the value)
def mass_button_wake():
    mass_variable1.set(mass_variable1.get())

mass_button = ttk.Button(tab1, text="Convert", width=69, command=mass_button_wake)
mass_button.pack(padx=5, pady=5)

def mass_swap():
    unit1 = mass_unit1.get()
    unit2 = mass_unit2.get()
    mass_unit1.set(unit2)
    mass_unit2.set(unit1)

mass_swapper = ttk.Button(tab1, text="Swap Units", width=69, command=mass_swap)
mass_swapper.pack(padx=5, pady=5)

#-------------------------------------------------LENGTH-------------------------------------------------

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
        length_multiplier = km_mi/(cm_m*m_km)
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
        length_multiplier = 1/(km_mi/(cm_m*m_km))
    if length_unit1.get() == 'Miles (mi)' and length_unit2.get() == 'Yard (yd)':
        length_multiplier = yd_mi
    if length_unit1.get() == 'Miles (mi)' and length_unit2.get() == 'Metres (m)':
        length_multiplier = 1/(km_mi/m_km)
    if length_unit1.get() == 'Miles (mi)' and length_unit2.get() == 'Kilometres (km)':
        length_multiplier = 1/km_mi
    if length_unit1.get() == 'Kilometres (km)' and length_unit2.get() == 'Inch (in)':
        length_multiplier = in_cm*m_km*cm_m
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
ttk.Label(tab2, text='', font=('Segoe', '15')).pack()

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

#--------------------------------------------------SPEED--------------------------------------------------
def speed_option_chosen(*args):
    global speed_multiplier
    if speed_unit1.get() == speed_unit2.get():
        speed_multiplier = 1
    if speed_unit1.get() == 'Miles per hour (mph)' and speed_unit2.get() == 'Kilometers per hour (kph)':
        speed_multiplier = mph_kph
    if speed_unit1.get() == 'Kilometers per hour (kph)' and speed_unit2.get() == 'Miles per hour (mph)':
        speed_multiplier = 1/mph_kph
    if speed_unit1.get() == 'Knots (kn)' and speed_unit2.get() == 'Kilometers per hour (kph)':
        speed_multiplier = kn_kph
    if speed_unit1.get() == 'Kilometers per hour (kph)' and speed_unit2.get() == 'Knots (kn)':
        speed_multiplier = 1/kn_kph
    if speed_unit1.get() == 'Miles per hour (mph)' and speed_unit2.get() == 'Knots (kn)':
        speed_multiplier = 1/kn_mph
    if speed_unit1.get() == 'Knots (kn)' and speed_unit2.get() == 'Miles per hour (mph)':
        speed_multiplier = kn_mph

def speed_calculate(value):
    value = value.get()
    value = float(value)*speed_multiplier
    speed_variable2.set(value)


tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Speed')
ttk.Label(tab3, text='', font=('Segoe', '15')).pack()

# DROPDOWNS

speed_options = ["Miles per hour (mph)",
                 "Kilometers per hour (kph)",
                 "Knots (kn)"]

speed_choices = ttk.Frame(tab3)
speed_choices.pack()

speed_unit1 = StringVar(speed_choices)
speed_unit1.trace("w", speed_option_chosen)

speed_unit2 = StringVar(speed_choices)
speed_unit2.trace("w", speed_option_chosen)

speed_choice1 = ttk.OptionMenu(speed_choices, speed_unit1, speed_options[0], *speed_options)
speed_choice1.config(width=30)
speed_choice1.grid(row=1, column=1, padx=5, pady=5)

speed_choice2 = ttk.OptionMenu(speed_choices, speed_unit2, speed_options[1], *speed_options)
speed_choice2.config(width=30)
speed_choice2.grid(row=1, column=2, padx=5, pady=5)

# ENTRY WIDGETS

speed_entries = ttk.Frame(tab3)
speed_entries.pack()

speed_variable1 = StringVar()
speed_variable2 = StringVar()
speed_variable1.trace("w", lambda name, index, mode, sv=speed_variable1: speed_calculate(speed_variable1))
speed_variable1.set(1)

speed_input1 = ttk.Entry(speed_entries, textvariable=speed_variable1)
speed_input1.grid(row=0, column=1, padx=5, pady=5)
speed_input1.config(width=34)

speed_input2 = ttk.Entry(speed_entries, textvariable=speed_variable2)
speed_input2.grid(row=0, column=2, padx=5, pady=5)
speed_input2.config(state='readonly', width=34)

# BUTTON (unnecessary, but will be nice to have when changing units and not changing the value)
def speed_button_wake():
    speed_variable1.set(speed_variable1.get())

speed_button = ttk.Button(tab3, text="Convert", width=69, command=speed_button_wake)
speed_button.pack(padx=5, pady=5)

def speed_swap():
    unit1 = speed_unit1.get()
    unit2 = speed_unit2.get()
    speed_unit1.set(unit2)
    speed_unit2.set(unit1)

speed_swapper = ttk.Button(tab3, text="Swap Units", width=69, command=speed_swap)
speed_swapper.pack(padx=5, pady=5)

#------------------------------------------------CURRENCY------------------------------------------------

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
tab_control.add(tab5, text='Currency')
ttk.Label(tab5, text='', font=('Segoe', '15')).pack()

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

currency_choice1 = ttk.OptionMenu(currency_choices, currency_unit1, currency_options[1], *currency_options)
currency_choice1.config(width=30)
currency_choice1.grid(row=1, column=1, padx=5, pady=5)

currency_choice2 = ttk.OptionMenu(currency_choices, currency_unit2, currency_options[0], *currency_options)
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

#------------------------------------------------TEMPERATURE------------------------------------------------

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
ttk.Label(tab4, text='', font=('Segoe', '15')).pack()

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

#------------------------------------------------CALENDAR------------------------------------------------

tab6 = ttk.Frame(tab_control)
tab_control.add(tab6, text='Date')
ttk.Label(tab6, text='', font=('Segoe', '9')).pack()

def jdn_to_gregorian(jdn):
    Q = float(jdn)+0.5
    Z = math.floor(Q)
    W = int((Z - 1867216.25)/36524.25)
    X = int(W/4)
    A = int(Z+1+W-X)
    B = int(A+1524)
    C = int((B-122.1)/365.25)
    D = int(365.25*C)
    E = int((B-D)/30.6001)
    F = int(30.6001*E)
    day = int(B-D-F+(Q-Z))
    month = E-1 if E<=13 else E-13
    year = C-4715 if month == 1 or month == 2 else C-4716
    # print(month)
    return (str("{0:0=2d}".format(month))) + '/' + (str("{0:0=2d}".format(day)) + '/' + str(year))
    # gregorian_cal_var.set(gregorian_date)

def gregorian_to_jdn(gregorian):
    Y = int(gregorian[-4:])
    M = int(gregorian[0:2])
    D = int(gregorian[3:5])
    A = Y/100
    B = A/4
    C = 2-A+B
    E = 365.25*(Y+4716)
    F = 30.6001*(M+1)
    jdn = C+D+E+F-1524.5
    # J = 367*Y-(7*(Y+5001+(M-9)/7))/4+(275*M)/9+D+1729777
    return(math.floor(jdn * 10 ** 1) / 10 ** 1)

def jdn_to_julian(jdn):
    jdn = float(jdn) + 0.5
    z = math.floor(jdn)
    a = z
    b = a + 1524
    c = math.floor((b - 122.1) / 365.25)
    d = math.floor(365.25 * c)
    e = math.floor((b - d) / 30.6001)

    month = math.floor((e - 1) if (e < 14) else (e - 13))
    year = math.floor((c - 4716) if (month > 2) else (c - 4715))
    day = b - d - math.floor(30.6001 * e)

    if (year < 1):
        year -= 1

    return (str("{0:0=2d}".format(month))) + '/' + (str("{0:0=2d}".format(day)) + '/' + str(year))

def julian_to_jdn(julian):
    Y = int(julian[-4:])
    M = int(julian[0:2])
    D = int(julian[3:5])

    if Y < 1:
        Y+= 1

    if M <= 2:
        Y-= 1
        M+= 12

    return((math.floor((365.25 * (Y + 4716))) + math.floor((30.6001 * (M + 1))) + D) - 1524.5)

def on_julianpressed():
    jdn_variable.set(julian_to_jdn(julian_cal_var.get()))
    gregorian_cal_var.set(jdn_to_gregorian(jdn_variable.get()))

def on_gregorianpressed():
    jdn_variable.set(gregorian_to_jdn(gregorian_cal.get()))
    julian_cal_var.set(jdn_to_julian(jdn_variable.get()))

def on_jdnpressed():
    julian_cal_var.set(jdn_to_julian(jdn_variable.get()))
    gregorian_cal_var.set(jdn_to_gregorian(jdn_variable.get()))
    print('traced')

date_widget = ttk.Frame(tab6)
date_widget.pack()

gregorian_cal_var = StringVar()
gregorian_cal = DateEntry(date_widget, textvariable=gregorian_cal_var,
                        width=32,
                        background='darkblue', 
                        foreground='white', 
                        borderwidth=0, 
                        year=2020, 
                        date_pattern='MM/dd/yyyy')
gregorian_cal.grid(row=2, column=1, padx=5, pady=5)
gregorian_cal_var.set('06/24/2020')
gregorian_entry = ttk.Button(date_widget, text="Gregorian Enter", width=32, command=on_gregorianpressed)
gregorian_entry.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(date_widget, text='Gregorian Date').grid(row=1, column=1, padx=0, pady=0)
# gregorian_label_var = StringVar(date_widget)
# gregorian_label = ttk.OptionMenu(date_widget, gregorian_label_var, 'Gregorian Date')
# gregorian_label.config(width=30, state='readonly')
# gregorian_label.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(date_widget, text='Julian Date').grid(row=1, column=2, padx=0, pady=0)
# julian_label_var = StringVar(date_widget)
# julian_label = ttk.OptionMenu(date_widget, julian_label_var, 'Julian Date')
# julian_label.config(width=30, state='readonly')
# julian_label.grid(row=1, column=2, padx=5, pady=5)

julian_cal_var = StringVar()
julian_cal = DateEntry(date_widget, textvariable=julian_cal_var,
                        width=32,
                        background='darkblue', 
                        foreground='white', 
                        borderwidth=0, 
                        year=2020, 
                        date_pattern='MM/dd/yyyy')
julian_cal_var.set('06/11/2020')
julian_cal.grid(row=2, column=2, padx=5, pady=5)
julian_entry = ttk.Button(date_widget, text="Julian Enter", width=32, command=on_julianpressed)
julian_entry.grid(row=3, column=2, padx=5, pady=5)

def date_button_wake():
    # date_variable1.set(date_variable1.get())
    print(gregorian_cal_var.get()[-4:])
    print(gregorian_cal_var.get()[0:2])
    print(gregorian_cal_var.get()[3:5])


jdn_entries = ttk.Frame(tab6)
jdn_entries.pack()

ttk.Label(jdn_entries, text='  Julian Day Number:').grid(row=0, column=0, padx=5, pady=5)

jdn_variable = StringVar()
jdn_variable.trace("w", lambda name, index, mode, sv=jdn_variable: on_jdnpressed())
jdn_variable.set(2459024.5)

jdn_input = ttk.Entry(jdn_entries, textvariable=jdn_variable)
jdn_input.grid(row=0, column=1, padx=5, pady=5)
jdn_input.config(width=52)

date_button = ttk.Button(tab6, text="Julian Day Number Enter", width=69, command=on_jdnpressed)
date_button.pack(padx=5, pady=5)

tab_control.pack(expand=1, fill='both')

window.mainloop()