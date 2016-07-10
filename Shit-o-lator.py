# The best shit-code calculator ever! ;-)
# v2.0!

print("######## Shit'o'lator v2.0! Enjoy! ;-) #########")
print("################################################\n")

# Checking of the digits
def digit_check(dig, n):
    try:
        float(dig)
        return (True)
    except (ValueError):
        if n == 1:
            digit_input(1)
        else:
            digit_input(2)

# Inputting of the digits
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

# Starts here. Inputting the first digit
digit_input(1)

# Inputing & checking the operation
oper_kind = {'+': [], '-': [], \
             '*': [], '/': []}
corr = False
while not corr:
    oper = input("Input the operation (+ - * /): ")
    for n in oper_kind:
        if oper == n:
            corr = True

# Inputting the second digit
digit_input(2)

oper_kind = {'+': float(dig1) + float(dig2),
             '-': float(dig1) - float(dig2),
             '*': float(dig1) * float(dig2),
             '/': float(dig1) / float(dig2)}

for n in oper_kind:
        if n == oper:
            sum = oper_kind[n]

if sum - int(sum) == 0:
    print()
    print("The result is: %i" % sum)
else:
    print()
    print("The result is: %f" % sum)

print("\n############# Have a nice day! ;-) #############")