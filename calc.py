#simple command line calculator project
operation = input('''
Please type the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# =============== Addition ===============
if operation =='+':
    print('{} + {}'.format(num1, num2))
    print(num1 + num2)

# =============== Subtraction ===============
elif operation =='-':
    print('{} - {}'.format(num1, num2))
    print(num1 - num2)

# =============== Multiplication ===============
elif operation =='*':
    print('{} * {}'.format(num1, num2))
    print(num1 * num2)

# =============== Division ===============
elif operation =='/':
    print('{} / {}'.format(num1, num2))
    print(num1 / num2)

else:
    print('You have not typed a valid opeartor')
