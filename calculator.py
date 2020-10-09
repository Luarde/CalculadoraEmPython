def calculate():
    operation = input(
'''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division

''')

    number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: '))

    result_1 = number_1 + number_2
    result_2 = number_1 * number_2
    result_3 = number_1 - number_2
    result_4 = number_1 / number_2

    if operation == '+':
        print(f'{number_1} + {number_2} = {result_1}')
    
    
    elif operation == '-': 
        print(f'{number_1} - {number_2} = {result_3}')
    

    elif operation == '*':
        print(f'{number_1} * {number_2} = {result_2}')
    

    elif operation == '/':
        print(f'{number_1} / {number_2} = {result_4}')
    
    else:
        print('You have not typed a valid operator, please run the program again \n')

calculate()

def again():
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    
    '''
    )

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()
again()