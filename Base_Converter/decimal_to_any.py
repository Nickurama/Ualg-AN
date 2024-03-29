import math

def convert_base(x, base):
    y = abs(x)

    if base <= 10:
        y = decimal_to_less_than_10(y, base)
        y = base_round(y, base)

    elif base <= 61:
        y = decimal_to_less_than_62(y, base)
        y = base_round(y, base)

    else:
        y = decimal_to_greater_than_61(y, base)


    if x < 0:
        y = "-" + y

    return y

def decimal_to_less_than_10(x, base):
    whole = decimal_to_less_than_10_whole(x, base)
    fractionary = decimal_to_less_than_10_fractionary(x, base)

    return whole + "," + fractionary

def decimal_to_less_than_10_whole(x, base):
    y = str(int(x))
    if x >= base:
        y = str(decimal_to_less_than_10_whole(x // base, base)) + str(int(x) % base)
    return y

def decimal_to_less_than_10_fractionary(x, base):
    y = ""
    for i in range(9):
        x -= int(x)
        x = x * base
        y += str(int(x))

    return y

def decimal_to_less_than_62(x, base):
    whole = decimal_to_less_than_62_whole(x, base)
    fractionary = decimal_to_less_than_62_fractionary(x, base)

    return whole + "," + fractionary

def decimal_to_less_than_62_whole(x, base):
    y = str(int(x))
    if x >= base:
        y = str(decimal_to_less_than_62_whole(x // base, base)) + int_to_alphanumeric(int(x) % base)
    else:
        y = int_to_alphanumeric(int(x))
    return y

def decimal_to_less_than_62_fractionary(x, base):
    y = ""
    for i in range(9):
        x -= int(x)
        x = x * base
        y += int_to_alphanumeric(int(x))
    return y

def decimal_to_greater_than_61(x, base):
    whole = decimal_to_greater_than_61_whole(x, base)
    fractionary = decimal_to_greater_than_61_fractionary(x, base)

    return whole + ";" + fractionary

def decimal_to_greater_than_61_whole(x, base):
    y = str(int(x))
    if x >= base:
        y = str(decimal_to_greater_than_61_whole(x // base, base)) + "," + str(int(x) % base)
    return y

def decimal_to_greater_than_61_fractionary(x, base):
    y = ""
    x -= int(x)
    x = x * base
    y += str(int(x))

    for i in range(7):
        x -= int(x)
        x = x * base
        y += "," + str(int(x))
    return y

def int_to_alphanumeric(x):
    if x >= 10 and x <= 35:
        return chr(x + 55)
    elif x >= 36 and x <= 61:
        return chr(x + 61)
    return str(x)

def alphanumeric_to_int(char):
    ascii_value = ord(char)
    result = 0
    if ascii_value >= 65 and ascii_value <= 90:
        result = int(ascii_value - 55)
    elif ascii_value >= 97 and ascii_value <= 122:
        result = int(ascii_value - 61)
    else:
        result = int(char)

    return result

def base_round(x, base):
    reverse = x[::-1]
    reverse_list = list(reverse)

    reverse_list.pop(0)
    if alphanumeric_to_int(reverse[0]) >= math.ceil(base / 2):
        reverse = reversed_base_string_list_add(reverse_list, base)

    reverse_list = remove_zeros(reverse_list)

    return "".join(reverse_list)[::-1]

def reversed_base_string_list_add(reverse_list, base):
    for i in range(len(reverse_list)):
        if reverse_list[i] == int_to_alphanumeric(base - 1):
            reverse_list[i] = "0"
        else:
            reverse_list[i] = chr(ord(reverse_list[i]) + 1)
            break
    return reverse_list

def remove_zeros(reverse_list):
    current_char = reverse_list[0]
    while current_char == "0":
        reverse_list.pop(0)
        current_char = reverse_list[0]
    if reverse_list[0] == ",":
        reverse_list.pop(0)
    return reverse_list

base = int(input("Select your base: "))
number = float(input("Select the number to convert: "))
print(convert_base(number, base))
