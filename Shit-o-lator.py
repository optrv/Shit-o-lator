# The best shit-code calculator ever! ;-)

print("#### The best shit'o'lator ever! Enjoy! ;-) ####")
print("################################################\n")

# Check of the digits
def digit_check(dig, n):
    try:
        float(dig)
        return (True)
    except (ValueError):
        print("Input the correct digit!\n")
        if n == 1:
            digit_input(1)
        else:
            digit_input(2)

# input the digits
def digit_input(n):
    cor = False
    while not cor:
        if n == 1:
            global dig1
            dig1 = input("Input the first digit: ")
            cor = digit_check(dig1, n)
            return dig1
        elif n == 2:
            global dig2
            dig2 = input("Input the second digit: ")
            cor = digit_check(dig2, n)
            return dig2

digit_input(1)

# Input, checking the operation & calculation
corr = False
while not corr:
    oper = input("Input the operation (+ - * /): ")

    if oper == '+':
        digit_input(2)
        print("The result is: ", float(dig1) + float(dig2))
        corr = True
    elif oper == '-':
        digit_input(2)
        print("The result is: ", float(dig1) - float(dig2))
        corr = True

    elif oper == '*':
        digit_input(2)
        print("The result is: ", float(dig1) * float(dig2))
        corr = True

    elif oper == '/':
        digit_input(2)
        if float(dig2) > 0:
            print("The result is: ", float(dig1) / float(dig2))
            corr = True
        else:
            print("You can't divide on zero!\n")
            continue
    else:
        print("Input the correct operation symbol!\n")

print("\n############# Have a nice day! ;-) #############")