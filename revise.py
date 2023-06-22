
# ====PRIME NUMBER====
def prime(x):
    if x <= 0:
        print(x, ' should be natural number to be prime')
    elif x == 1:
        print('1 is not a prime number')
    else:
        f = 0
        for i in range(2, x):
            if x % i == 0:
                f = 1
        if f == 1:
            print(x, ' is not a prime number')
        else:
            print(x, ' is a prime number')


# ====TWISTED PRIME NUMBER====
def twisted_prime(x):
    if x <= 0:
        print(x, ' should be natural number to be twisted prime number')
    elif x == 1:
        print('1 is not a twisted prime numbe')
    else:
        f = 0
        for i in range(2, x):
            if x % i == 0:
                f = 1
        if f == 1:
            print(x, ' is not a prime and twisted prime number')
        else:
            str_x = ''
            for i in str(x):
                str_x = i + str_x
            k = 0
            for i in range(2, int(str_x)):
                if int(str_x) % i == 0:
                    k = 1
            if k == 1:
                print(x, ' is a prime number but not twisted prime number')
            else:
                print(x, ' is  a twisted prime number')


# ====MAGIC NUMBER====
def magic(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    if sum < 10:
        if sum == 1:
            print(x, 'is a magic number')
        else:
            print(x, 'is not a magic number')
    else:
        magic(sum)


# ====AMSTRONG NUMBER====
def amstrong(x):
    a = 0
    b = 0
    for i in str(x):
        a += 1
    for i in str(x):
        b += int(i)**a
    if b == x:
        print(x, ' is a amstrong number')
    else:
        print(x, ' is not a amstrong number')


# ====PERFECT NUMBER====
def perfect(x):
    list = []
    for i in range(1, x):
        if x % i == 0:
            list.append(i)
    k = 0
    for i in list:
        k += int(i)
    if k == x:
        print(x, 'is a perfect number')
    else:
        print(x, ' is not a prime number')


# ====PALLENDROME NUMBER====
def pallendrome(x):
    k = str(x)
    str1 = ''
    for i in k:
        str1 = i + str1
    if str1 == k:
        print(x, 'is a pallendrome number')
    else:
        print(x, 'is not a pallendrome number')


# ====FIBONACCI NUMBER====
def fibonacci(x):
    a, b, c = 1, 1, 0
    while (c <= x):
        c = a + b
        print(a, ' + ', b, ' = ', c)
        a = b
        b = c


# ====GUESS THE RANDOM NUMBER GAME====
def random_number_guess_game():
    import random
    a = random.randint(1, 100)
    b = int(input('guess the number\n'))
    c = 0
    while a != b:
        if b > a:
            c += 1
            b = int(
                input('you guessed the larger number please guess the smaller value\n'))
        else:
            c += 1
            b = int(
                input('you guessed the smaller number please guess the larger value\n'))
    print(f'finally you guessed the right numer : {a}')
    if c >= 5:
        print(f'noob you take {c} chances to guess :/')
    else:
        print(f'NOICE !! you r good at this :) \n you take only {c} chances')


# ====ROCK PAPER SCISSOR (NOT A SEPRATE UI)====
def rock_paper_scissor():
    import random
    run = 1
    while run:
        a = int(input('_____________________\n|enter 0 for rock   |\n|                   |\n|enter 1 for paper  |\n|                   |\n|enter 2 for scissor|\n|___________________|\n :- '))
        l = ['Rock', 'Paper', 'Scissor']
        b = random.choice(l)
        a = l[a]
        if a == 'Rock' and b == 'scissor':
            print(f'win machine entered {b}')
        elif a == 'Paper' and b == 'Rock':
            print(f'win machine entered {b}')
        elif a == 'Scissor' and b == 'Paper':
            print(f'Win machine entered {b}')
        else:
            print(f'lose machine entered {b}')

        run = int(input('enter 1 to continue and 0 to stop'))
