print("Basic Calculator - Jeyers Development")


while True:
    inpt1 = input("#: ")
    symbol = input('+, -, *, /: ')
    inpt2 = input("#: ")

    if '+' == symbol: print(inpt1 + " + " + inpt2 + " = " + str(int(inpt1) + int(inpt2)))
    elif '-' == symbol: print(inpt1 + " - " + inpt2 + " = " + str(int(inpt1) - int(inpt2)))
    elif '*' == symbol: print(inpt1 + " x " + inpt2 + " = " + str(int(inpt1) * int(inpt2)))
    elif '/' == symbol: print(inpt1 + " / " + inpt2 + " = " + str(int(inpt1) / int(inpt2)))