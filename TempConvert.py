#Marc Joseph Ramos
import temp_formula as tform

unit = 0
while unit == 0:
    to_convert = input("Input Temperature (with unit) to convert: ")
    to_convert = to_convert.upper()
    try:
        if 'C' in to_convert and 'F' not in to_convert and 'K' not in to_convert:
            unit = 'C'
        elif 'F' in to_convert and 'C' not in to_convert and 'K' not in to_convert:
            unit = 'F'
        elif 'K' in to_convert and 'F' not in to_convert and 'C' not in to_convertd:
            unit = 'K'
        else:
            raise Exception
        str(unit)
        to_convert = to_convert.removesuffix(unit)
        to_convert = float(to_convert)
    except:
        print("Wrong Input!")
        unit = 0


choice = 0
while choice != 1 and choice != 2:
    try:
        if unit == 'C':
            choice = int(input("Choose the number in which you wanna convert to:\n1. Convert to F\n2. Convert to K\nChoice: "))
        elif unit == 'F':
            choice = int(input("Choose the number in which you wanna convert to:\n1. Convert to C\n2. Convert to K\nChoice: "))
        elif unit == 'K':
            choice = int(input("Choose the number in which you wanna convert to:\n1. Convert to F\n2. Convert to C\nChoice: "))
        if choice != 1 and choice != 2:
            choice = 0
            raise Exception
    except:
        print("Wrong Input!")
        choice = 0

converted = 0.0
converted_unit = 0
if unit == 'C':
    if choice == 1:
        converted = tform.C_to_F(to_convert)
        converted_unit = 'F'
    else:
        converted = tform.C_to_K(to_convert)
        converted_unit = 'K'
elif unit == 'F':
    if choice == 1:
        converted = tform.F_to_C(to_convert)
        converted_unit = 'C'
    else:
        converted = tform.F_to_K(to_convert)
        converted_unit = 'K'
else:
    if choice == 1:
        converted = tform.K_to_F(to_convert)
        converted_unit = 'F'
    else:
        converted = tform.K_to_C(to_convert)
        converted_unit = 'C'

print("%.2f %s is %.2f %s" % (to_convert, unit, converted, converted_unit))
