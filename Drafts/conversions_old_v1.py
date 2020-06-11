def w_convert():
    kg_lb = 2.2046228
    st_lb = 14
    st_kg = 6.3502927

    conv_choice = input(
                "Choose from one of the following weight conversions:\n"
                "1. Pound (lb) <-> Kilogram (kg)\n"
                "2. Stone (st) <-> Pound (lb)\n"
                "3. Stone (st) <-> Kilogram (kg)\n\n"
                
                "Choice: ")

    if conv_choice == '1':
        entry = input(
                "\n"
                "Enter a value, followed by a unit. (e.g.: 15lbs or 1lb or 23kg)\n\n"
                "Value: ")

        def lbconvert():
            output = entry/kg_lb
            
            if entry > 1 or entry < 1:
                unit = 'lbs'
            elif entry == 1:
                unit = 'lb'

            print(
                str(entry) + unit + " equal to " +
                str(output) + "kg."
            )
        def kgconvert():
            output = entry*kg_lb

            print(
                str(entry) + "kg equal to " +
                str(output) + "lbs."
            )

        if entry[-3:] == 'lbs':
            unit =  'lbs'
            entry = float(entry[:-3])
            lbconvert()
        elif entry[-2:] == 'lb':
            unit =  'lb'
            entry = float(entry[:-2])
            lbconvert()
        elif entry[-2:] == 'kg':
            entry = float(entry[:-2])
            kgconvert()

        

w_convert()