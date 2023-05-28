l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_update():
    grid = (f" {l[0]} | {l[1]} | {l[2]} \n===========\n {l[3]} | {l[4]} | {l[5]} \n===========\n {l[6]} | {l[7]} | {l[8]}")
    print(grid)

conditions = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [1, 4, 7],
              [2, 5, 8],
              [3, 6, 9],
              [1, 5, 9],
              [3, 5, 7]]

def check_win(a : str) -> str :
    global run
    for i in conditions:
        j = 0
        for k in i:
            if l[k - 1] == a:
                j += 1
        if j > 2:
            print()
            print(f'{a} win')
            run = False
            break

print_update()
run = True

while run:
    print()
    O = int(input('enter place according to number in grid for O :- '))
    l[O - 1] = 'O'
    check_win('O')
    if run == False:
        break
    print_update()
    print()

    X = int(input('enter place according to number in grid for X :- '))
    if l[X - 1] == 'O':
        print()
        print('CHEATING NAHI AB TERI CHANCE GAYI :)')
    else:
        l[X - 1] = 'X'
        check_win('X')
        print_update()
