import calc
condition = True

while condition:
    with open('menu.txt') as menu:
        for line in menu:
            print(line.strip())

    condition = calc.app()


