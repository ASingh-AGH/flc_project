def infix_to_rpn(expression):
    # Set up the precedence of the operators
    precedence = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1,
        "^": 2,
        "(": 3,
        ")": 3
    }

    # Set up the stack for the Shunting-yard algorithm
    stack = []
    output = []

    # Iterate through the expression one character at a time
    for c in expression:
        if c.isdigit() or c.isalpha():
            output.append(c)
        # If the character is an operator, pop from stack based on precedence
        elif c in precedence:
            while stack and stack[-1] != "(" and precedence[stack[-1]] >= precedence[c]:
                output.append(stack.pop())
            stack.append(c)

        elif c == "(":
            stack.append(c)
        # If the character is a right parenthesis, pop all the operators from
        # the stack until you reach the matching left parenthesis
        elif c == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()


    # Pop remaining operators from the stack and add them to the output
    while stack:
        output.append(stack.pop())

    output = [s.replace('(', '') and s.replace(')', '') for s in output]
    # Return the result as a string
    return " ".join(output)

def tempchoice():
    tmpchoice = input('Go back to the menu? (y/n) ')
    return 0 if tmpchoice == 'y' else 4

def main():

    choice =''    
    while choice != '4':

        print ('-------------------------------------------------')
        print ('Welcome to the reverse polish notation calculator')
        print ('-------------------------------------------------')
        print ('1. Test example input cases')
        print ('2. User input')
        print ('3. About the project')
        print ('4. Quit')

        choice = input('Enter a choice (1-4): ')
        
        if choice == '1':

            # use in separate file to generate more batches ^(.+)$
            # suggestion to make more complex would be to have a valid random generator for expressions


            print ('-------------------------------------------------')
            print ('Test example input cases:')
            print ('-------------------------------------------------')
            print ('Alphabetical expressions')
            #ALPABET TEST
            print ('-------------------------------------------------')
            print(infix_to_rpn('a + b * c / ( d - e ) ^ f'))
            print(infix_to_rpn('g - h * ( i + j ) / k ^ l'))
            print(infix_to_rpn('m + n * ( o - p ) / q ^ r'))
            print(infix_to_rpn('s / t + u * v - w ^ x'))
            print(infix_to_rpn('y - z / aa + bb * cc ^ dd'))
            print(infix_to_rpn('ee * ff + gg / hh - ii ^ jj'))
            print(infix_to_rpn('kk / ll - mm + nn * oo ^ pp'))
            print(infix_to_rpn('qq - rr / ss + tt * uu ^ vv'))
            print(infix_to_rpn('( ww + xx ) * yy / ( zz - aaa ) ^ bbb'))
            print(infix_to_rpn('ccc * ddd + eee / fff - ggg ^ hhh'))
            print(infix_to_rpn('iii - jjj / kkk + lll * mmm ^ nnn'))
            print(infix_to_rpn('ooo + ppp / qqq - rrr * sss ^ ttt'))
            print(infix_to_rpn('uuu * vvv + www / xxx - yyy ^ zzz'))
            print(infix_to_rpn('aaaa / bbbb - cccc + dddd * eeee ^ ffff'))
            print(infix_to_rpn('gggg - hhhh / iii + jjjj * kkkk ^ llll'))
            print ('-------------------------------------------------')
            #INT TEST

            print ('Integer expressions')

            print ('-------------------------------------------------')
            print(infix_to_rpn('1 + 2 * 3 / ( 4 - 5 ) ^ 6'))
            print(infix_to_rpn('7 - 8 * ( 9 + 10 ) / 11 ^ 12'))
            print(infix_to_rpn('13 + 14 * ( 15 - 16 ) / 17 ^ 18'))
            print(infix_to_rpn('19 / 20 + 21 * 22 - 23 ^ 24'))
            print(infix_to_rpn('25 - 26 / 27 + 28 * 29 ^ 30'))
            print(infix_to_rpn('31 + 32 / 33 - 34 * 35 ^ 36'))
            print(infix_to_rpn('37 * 38 + 39 / 40 - 41 ^ 42'))
            print(infix_to_rpn('43 / 44 - 45 + 46 * 47 ^ 48'))
            print(infix_to_rpn('( 49 + 50 ) * 51 / ( 52 - 53 ) ^ 54'))
            print(infix_to_rpn('55 * 56 + 57 / 58 - 59 ^ 60'))
            print(infix_to_rpn('61 - 62 / 63 + 64 * 65 ^ 66'))
            print(infix_to_rpn('67 + 68 / 69 - 70 * 71 ^ 72'))
            print(infix_to_rpn('73 * 74 + 75 / 76 - 77 ^ 78'))
            print(infix_to_rpn('79 / 80 - 81 + 82 * 83 ^ 84'))
            print(infix_to_rpn('85 - 86 / 87 + 88 * 89 ^ 90'))
            print ('-------------------------------------------------')
            #FLOAT TEST

            print ('Floating point expressions')
            
            print ('-------------------------------------------------')
            print(infix_to_rpn('6.7 + 7.8 / 8.9 - 9.1 * 1.2 ^ 2.3'))
            print(infix_to_rpn('3.4 * 4.5 + 5.6 / 6.7 - 7.8 ^ 8.9'))
            print(infix_to_rpn('9.1 / 1.2 - 2.3 + 3.4 * 4.5 ^ 5.6'))
            print(infix_to_rpn('6.7 - 7.8 / 8.9 + 9.1 * 1.2 ^ 2.3'))
            print(infix_to_rpn('( 3.4 + 4.5 ) * 5.6 / ( 6.7 - 7.8 ) ^ 8.9'))
            print(infix_to_rpn('9.1 * 1.2 + 2.3 / 3.4 - 4.5 ^ 5.6'))
            print(infix_to_rpn('6.7 - 7.8 / 8.9 + 9.1 * 1.2 ^ 2.3'))
            print(infix_to_rpn('3.4 + 4.5 / 5.6 - 6.7 * 7.8 ^ 8.9'))
            print(infix_to_rpn('9.1 * 1.2 + 2.3 / 3.4 - 4.5 ^ 5.6'))
            print(infix_to_rpn('6.7 / 7.8 - 8.9 + 9.1 * 1.2 ^ 2.3'))
            print(infix_to_rpn('3.4 - 4.5 / 5.6 + 6.7 * 7.8 ^ 8.9'))
            print(infix_to_rpn('9.1 + 1.2 / 2.3 - 3.4 * 4.5 ^ 5.6'))
            print(infix_to_rpn('6.7 * 7.8 + 8.9 / 9.1 - 1.2 ^ 2.3'))
            print(infix_to_rpn('3.4 / 4.5 - 5.6 + 6.7 * 7.8 ^ 8.9'))
            print(infix_to_rpn('9.1 - 1.2 / 2.3 + 3.4 * 4.5 ^ 5.6'))
            print ('-------------------------------------------------')

            choice = tempchoice()

        elif choice == '2':
            expression = input('Enter an expression in infix notation: ')
            result = infix_to_rpn(expression)
            #print('Reverse Polish notation:', rpn)
            print(f'Reverse Polish notation: {result}')
            choice = tempchoice()

        elif choice == '3':

            print ('-------------------------------------------------')
            print ('About the project')
            print ('-------------------------------------------------')
            print ('Final FLC project 2022/23 Pierre Rheeder & Apoorva Singh')
            print ('Coded in Python')
            print ('-------------------------------------------------')
            print ('Accepts int, float and alphabetical inputs as mathematical expression')
            print ('Sent to Fuction infix_to_rpn in the form of a string')
            print ('Outputs mathematical expressions from infix notation to reverse Polish notation')
            print ('-------------------------------------------------')
        
            choice = tempchoice()
            

        elif choice == '4':
                print('Quitting the program...') # auto quit while loop
        else:
                print('Invalid choice! Please enter a number between 1 and 4.')

if __name__ == '__main__':
    main()
