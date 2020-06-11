import math

def w_convert():
    kg_lb = 2.2046228
    st_lb = 14
    st_kg = 6.3502927

    conv_choice = input(
        "Choose the unit to convert from:\n"
        "   1. Kilogram (kg)\n"
        "   2. Pounds   (lb)\n"
        "   3. Stone    (st)\n\n"

        "Choice: "
    )

    entry_value = float(input(
        "\n"
        "Enter your value to be converted.\n\n"
        "Value: "
    ))

    output_unit = input(
        "Choose the unit to convert to:\n"
        "   1. Kilogram (kg)\n"
        "   2. Pounds   (lb)\n"
        "   3. Stone    (st)\n\n"

        "Choice: "
    )

    if conv_choice == output_unit:
        print("The units chosen are the same, please re-enter a different unit to convert from and to.")
        w_convert()

    elif conv_choice == '1' and output_unit == '2':
        output_value = entry_value*kg_lb
        print(str(entry_value) + 'kg is equal to ' +  str(output_value) + 'lb(s).')

    elif conv_choice == '2' and output_unit == '1':
        output_value = entry_value/kg_lb
        print(str(entry_value) + 'lb is equal to ' +  str(output_value) + 'kg.')

    elif conv_choice == '3' and output_unit == '2':
        output_value = entry_value*st_lb
        print(str(entry_value) + 'st is equal to ' +  str(output_value)+ 'lb(s).')

    elif conv_choice == '2' and output_unit == '3':
        output_value = entry_value/st_lb
        print(str(entry_value) + 'lb is equal to ' +  str(output_value) + 'st.')

    elif conv_choice == '3' and output_unit == '1':
        output_value = entry_value*st_kg
        print(str(entry_value) + 'st is equal to ' +  str(output_value) + 'kg.')

    elif conv_choice == '1' and output_unit == '3':
        output_value = entry_value/st_kg
        print(str(entry_value) + 'kg is equal to ' +  str(output_value) + 'st.')

def l_convert():
    cm_in = 0.39370
    m_yd  = 1.0936
    km_mi = 0.62137

    conv_choice = input(
        "Choose the unit conversion:\n"
        "   1. Centimeter  (cm)  ->  Inches      (in)\n"
        "   2. Inches      (in)  ->  Centimeter  (cm)\n"
        "   3. Meters       (m)  ->  Yards       (yd)\n"
        "   4. Yards       (yd)  ->  Meters       (m)\n"
        "   5. Miles       (mi)  ->  Kilometers  (km)\n"
        "   6. Kilometers  (km)  ->  Miles       (mi)\n\n"

        "Choice: "
    )

    entry_value = float(input(
        "\n"
        "Enter your value to be converted.\n\n"
        "Value: "
    ))

    if conv_choice == '1':
        output_value = entry_value * cm_in
        print(str(entry_value) + 'cm is equal to ' +  str(output_value) + 'in.')
    elif conv_choice == '2':
        output_value = entry_value / cm_in
        print(str(entry_value) + 'in is equal to ' +  str(output_value) + 'cm.')
    elif conv_choice == '3':
        output_value = entry_value * m_yd
        print(str(entry_value) +  'm is equal to ' +  str(output_value) + 'yd.')
    elif conv_choice == '4':
        output_value = entry_value / m_yd
        print(str(entry_value) + 'yd is equal to ' +  str(output_value) + 'm.' )
    elif conv_choice == '5':
        output_value = entry_value / km_mi
        print(str(entry_value) + 'mi is equal to ' +  str(output_value) + 'km.')
    elif conv_choice == '6':
        output_value = entry_value * km_mi
        print(str(entry_value) + 'km is equal to ' +  str(output_value) + 'mi.')

def s_convert():
    mph_kph = 1.609344
    kn_mph  = 1.1507795
    kn_kph  = 1.852

    conv_choice = input(
        "Choose the unit to convert from:\n"
        "   1. Miles per hour       (mph)\n"
        "   2. Kilometers per hour  (kph)\n"
        "   3. Knots                ( kn)\n\n"

        "Choice: "
    )

    entry_value = float(input(
        "\n"
        "Enter your value to be converted.\n\n"
        "Value: "
    ))

    output_unit = input(
        "Choose the unit to convert to:\n"
        "   1. Miles per hour       (mph)\n"
        "   2. Kilometers per hour  (kph)\n"
        "   3. Knots                ( kn)\n\n"

        "Choice: "
    )

    if conv_choice == output_unit:
        print("The units chosen are the same, please re-enter a different unit to convert from and to.")
        w_convert()

    elif conv_choice == '1' and output_unit == '2':
        output_value = entry_value * mph_kph
        print(str(entry_value) + 'mph is equal to ' +  str(output_value) + 'kph.')
    elif conv_choice == '2' and output_unit == '1':
        output_value = entry_value / mph_kph
        print(str(entry_value) + 'kph is equal to ' +  str(output_value) + 'mph.')
    elif conv_choice == '3' and output_unit == '1':
        output_value = entry_value * kn_mph
        print(str(entry_value) +  'kn is equal to ' +  str(output_value) + 'mph.')
    elif conv_choice == '1' and output_unit == '3':
        output_value = entry_value / kn_mph
        print(str(entry_value) + 'mph is equal to ' +  str(output_value) +  'kn.')
    elif conv_choice == '3' and output_unit == '2':
        output_value = entry_value * kn_kph
        print(str(entry_value) +  'kn is equal to ' +  str(output_value) + 'kph.')
    elif conv_choice == '2' and output_unit == '3':
        output_value = entry_value / kn_kph
        print(str(entry_value) + 'kph is equal to ' +  str(output_value) +  'kn.')

def t_convert():
    FC_multiplier = 1.8000
    FC_addend = 32.00
    KC_addend = 273.15

    conv_choice = input(
        "Choose the unit to convert from:\n"
        "   1. Fahrenheit   (" u"\N{DEGREE SIGN}" "F)\n"
        "   2. Celsius      (" u"\N{DEGREE SIGN}" "C)\n"
        "   3. Kelvin       ( K)\n\n"

        "Choice: "
    )

    entry_value = float(input(
        "\n"
        "Enter your value to be converted.\n\n"
        "Value: "
    ))

    output_unit = input(
        "Choose the unit to convert to:\n"
        "   1. Fahrenheit   (" u"\N{DEGREE SIGN}" "F)\n"
        "   2. Celsius      (" u"\N{DEGREE SIGN}" "C)\n"
        "   3. Kelvin       ( K)\n\n"

        "Choice: "
    )

    if conv_choice == output_unit:
        print("The units chosen are the same, please re-enter a different unit to convert from and to.")
        t_convert()

    elif conv_choice == '1' and output_unit == '2':
        output_value = (entry_value-FC_addend)/FC_multiplier
        print(str(entry_value) + u'\N{DEGREE SIGN}' + 'F is equal to ' +  str(output_value) + u'\N{DEGREE SIGN}' + 'C.')

    elif conv_choice == '2' and output_unit == '1':
        output_value = (entry_value*FC_multiplier) + FC_addend
        print(str(entry_value) + u'\N{DEGREE SIGN}' + 'C is equal to ' +  str(output_value) + u'\N{DEGREE SIGN}' + 'F.')

    elif conv_choice == '3' and output_unit == '2':
        output_value = entry_value - KC_addend
        print(str(entry_value) + 'K is equal to ' +  str(output_value) + u'\N{DEGREE SIGN}' + 'C.')

    elif conv_choice == '2' and output_unit == '3':
        output_value = entry_value + KC_addend
        print(str(entry_value) + u'\N{DEGREE SIGN}' + 'C is equal to ' +  str(output_value) + 'K.')

    elif conv_choice == '3' and output_unit == '1':
        output_value = ((entry_value - KC_addend)*FC_multiplier) + FC_addend
        print(str(entry_value) + 'K is equal to ' +  str(output_value) + u'\N{DEGREE SIGN}' + 'F.')

    elif conv_choice == '1' and output_unit == '3':
        output_value = ((entry_value - FC_addend)/FC_multiplier) + KC_addend
        print(str(entry_value) + u'\N{DEGREE SIGN}' + 'F is equal to ' +  str(output_value) + 'K.')

def c_convert():
    aed_usd = 3.67
    aed_gbp = 4.65
    usd_gbp = 1.27

    conv_choice = input(
        "Choose the currency to convert from:\n"
        "   1. United Arab Emirates Dirham  (AED)\n"
        "   2. United States Dollar         (USD)\n"
        "   3. Pound Sterling               (GBP)\n\n"

        "Choice: "
    )

    entry_value = float(input(
        "\n"
        "Enter your value to be converted.\n\n"
        "Value: "
    ))

    output_unit = input(
        "Choose the currency to convert to:\n"
        "   1. United Arab Emirates Dirham  (AED)\n"
        "   2. United States Dollar         (USD)\n"
        "   3. Pound Sterling               (GBP)\n\n"

        "Choice: "
    )

    if conv_choice == output_unit:
        print("The units chosen are the same, please re-enter a different unit to convert from and to.")
        w_convert()

    elif conv_choice == '1' and output_unit == '2':
        output_value = entry_value / aed_usd
        print(str(entry_value) + 'AED is equal to ' +  str(round(output_value , 2)) + 'USD.')

    elif conv_choice == '2' and output_unit == '1':
        output_value = entry_value * aed_usd
        print(str(entry_value) + 'USD is equal to ' +  str(round(output_value , 2)) + 'AED.')

    elif conv_choice == '1' and output_unit == '3':
        output_value = entry_value * aed_gbp
        print(str(entry_value) + 'AED is equal to ' +  str(round(output_value , 2)) + 'GBP.')

    elif conv_choice == '3' and output_unit == '1':
        output_value = entry_value / aed_gbp
        print(str(entry_value) + 'GBP is equal to ' +  str(round(output_value , 2)) + 'AED.')

    elif conv_choice == '2' and output_unit == '3':
        output_value = entry_value / usd_gbp
        print(str(entry_value) + 'USD is equal to ' +  str(round(output_value , 2)) + 'GBP.')

    elif conv_choice == '3' and output_unit == '2':
        output_value = entry_value * usd_gbp
        print(str(entry_value) + 'GBP is equal to ' +  str(round(output_value , 2)) + 'USD.')

def d_convert():
    Y = int(input("year: "))
    M = int(input("month: "))
    D = int(input("day: "))
    A = Y/100
    B = A/4
    C = 2-A+B
    E = 365.25*(Y+4716)
    F = 30.6001*(M+1)
    J = C+D+E+F-1524.5
    # J = 367*Y-(7*(Y+5001+(M-9)/7))/4+(275*M)/9+D+1729777
    print(J)

    def jd_to_julian(J):
    
        J += 0.5
        z = math.floor(J)
    
        a = z
        b = a + 1524
        c = math.floor((b - 122.1) / 365.25)
        d = math.floor(365.25 * c)
        e = math.floor((b - d) / 30.6001)
    
        month = math.floor((e - 1) if (e < 14) else (e - 13))
        year = math.floor((c - 4716) if (month > 2) else (c - 4715))
        day = b - d - math.floor(30.6001 * e)
    
        '''If year is less than 1, subtract one to convert from
            a zero based date system to the common era system in
            which the year -1 (1 B.C.E) is followed by year 1 (1 C.E.).'''
    
        if (year < 1):
            year -= 1
    
        print (year, month, day)
    


    jd_to_julian(J)