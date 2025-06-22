import mathu

def app():
    selection = input('Which menu would you like to do? ')

    if selection == '5':
        return False

    n1 = int(input('What is the first number? '))
    n2 = int(input('What is the second number? '))
    print('\n')

    if selection == '1':
        print('The result is: ')
        print(mathu.add(n1, n2))

    elif selection == '2':
        print(mathu.sub(n1, n2))

    elif selection == '3':
        print(mathu.mult(n1, n2))

    elif selection == '4':
        print(mathu.div(n1, n2))



    condition = input('\nWould like to continue? Y - N: ').lower()
    if condition == 'n':
        return False
    else: return True
