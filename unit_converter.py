#Conversion functions
def convert(fro, to, val):
    if fro == "C" and to == "F":
        return val * 1.8 + 32
    elif fro == "F" and to == "C":
        return (val - 32) / 1.8
    elif fro == "in" and to =="cm":
        return val * 2.54
    elif fro =="ft" and to == "cm":
        return val* 30.48
    elif fro == "mi" and to =="km":
        return val * 1.61
    elif fro =="scm" and to =="km":
        return val * 10
    elif fro == "lb" and to == "kg":
        return val * 0.45
    elif fro == "m" and to == "ft": 
        return val * 3.28
    elif fro == "km" and to == "mi":
        return val * 0.62
    elif fro == "kg" and to == "lb":
        return val * 2.2
    else:
        return val