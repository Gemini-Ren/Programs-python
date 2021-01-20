def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
1 for addition
2 for subtraction
3 for multiplication
4 for division
''')

    numero_1 = int(input('primeiro numero: '))
    numero_2 = int(input('segundo numero: '))

    if operation == '1':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operation == '2':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operation == '3':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operation == '4':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function

calculate()

'''
Renan Corrêa Sant'Anna

'''