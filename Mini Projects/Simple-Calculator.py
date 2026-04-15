# A simple Arithmetic Calculator

# Takes Input of Numbers
num_1 = float(input('Enter Your First Number\n'))
num_2 = float(input('\nEnter Your Second Number\n'))

# Asks for Which Operation
operation = input('''\nHere is the List of Operations : 

Addition       : 1
Subtraction    : 2
Multiplication : 3
Divison        : 4
Floor Divison  : 5
Find Remainder : 6
Exponentiation : 7
Percentage     : 8

Press the Number of Operation You Would Like To Do.\t''')

print('\n')

# Executes the selected Operation
match operation :
    case '1' :
        print(num_1,'+', num_2,':',num_1+num_2 )
    case '2' :
        print(num_1,'-', num_2, ':', num_1-num_2)
    case '3' :
        print(num_1, '*', num_2, ':', num_1*num_2)
    case '4' :
        print(num_1, '/', num_2, ':', num_1/num_2)
    case '5' :
        print(num_1, 'Floor Divisioned By', num_2, ':', num_1//num_2)
    case '6' :
        print('Remainder of ',num_1, '/',num_2, ':', num_1%num_2)
    case '7' :
        print(num_1, 'Exponentiated by', num_2, ':', num_1**num_2)
    case '8' :
        print(num_1, '% of', num_2, ':', num_1 * num_2 / 100)
    case _ if (int(operation) > 9) :
        print('Error Found. Retry.')