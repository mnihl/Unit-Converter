#Conversion functions
def convert(fro, to, val):
    orig_val = val
    if fro == "C" and to == "F":
        result = val * 1.8 + 32
    elif fro == "F" and to == "C":
        result = (val - 32) / 1.8
    elif fro == "in" and to =="cm":
        result = val * 2.54
    elif fro =="ft" and to == "cm":
        result = val* 30.48
    elif fro == "mi" and to =="km":
        result = val * 1.61
    elif fro =="scm" and to =="km":
        result = val * 10
    elif fro == "lb" and to == "kg":
        result = val * 0.45
    elif fro == "m" and to == "ft": 
        result = val * 3.28
    elif fro == "km" and to == "mi":
        result = val * 0.62
    elif fro == "kg" and to == "lb":
        result = val * 2.2
    else:
        return "Conversion not possible, please try other units"
    
    return f"{orig_val}{fro} converted to {to} is {result}{to}"

user_val = input("Enter the value you want to convert (e.g. 5): ")
user_fro = input("Enter the unit you want to convert from (e.g. C): ")
user_to = input("Enter the unit you want to convert to (e.g. F): ")
print(convert(user_fro, user_to, float(user_val)))