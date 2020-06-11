from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkcalendar import Calendar, DateEntry
import math


window = ThemedTk(theme="breeze")
tab_control = ttk.Notebook(window)

tab6 = ttk.Frame(tab_control)
tab_control.add(tab6, text='Date')

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

ttk.Label(date_widget, text='Gregorian Date').grid(row=1, column=1, padx=5, pady=5)
# gregorian_label_var = StringVar(date_widget)
# gregorian_label = ttk.OptionMenu(date_widget, gregorian_label_var, 'Gregorian Date')
# gregorian_label.config(width=30, state='readonly')
# gregorian_label.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(date_widget, text='Julian Date').grid(row=1, column=2, padx=5, pady=5)
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
jdn_variable.trace("w", lambda name, index, mode, sv=jdn_variable: jdn_to_julian(float(jdn_variable.get())))
jdn_variable.set(2459024.5)

jdn_input = ttk.Entry(jdn_entries, textvariable=jdn_variable)
jdn_input.grid(row=0, column=1, padx=5, pady=5)
jdn_input.config(width=52)

date_button = ttk.Button(tab6, text="Julian Day Number Enter", width=69, command=on_jdnpressed)
date_button.pack(padx=5, pady=5)

tab_control.pack(expand=1, fill='both')

window.mainloop()