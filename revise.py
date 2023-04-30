
#prime number checker
def prime(x):
    if x <= 0:
        print(x, ' should be natural number to be prime')
    else:
        f = 0
        for i in range(2, x):
            if x % i == 0:
                f = 1
        if f == 1:
            print(x, ' is not a prime number')
        else:
            print(x, ' is a prime number')

#twister prime checker
def twisted_prime(x):
    if x <= 0:
        print(x, ' should be natural number to be twisted_prime')
    else:
        f = 0
        for i in range(2, x):
            if x % i == 0:
                f = 1
        if f == 1:
            print(x, ' is not a prime and twisted_prime number')
        else:
            str_x = ''
            for i in str(x):
                str_x = i + str_x
            k = 0
            for i in range(2, int(str_x)):
                if int(str_x) % i == 0:
                    k = 1
            if k == 1:
                print(x, ' is a prime number but not twisted_prime number')
            else:
                print(x, ' is  a twisted_prime number')

                
#magic number checker
def magic(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    if sum < 10:
        if sum == 1:
            print('magic number')
        else:
            print('not magic number')
    else:
        magic(sum)

#amstrong number checker
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

#perfect number checker
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

#pallendrome numbers checker
def pallendrome(x):
    k = str(x)
    str1 = ''
    for i in k:
        str1 = i + str1
    if str1 == k:
        print(x, 'is a pallendrome number')
    else:
        print(x, 'is not a pallendrome number')

#fibonacci series
def fibonacci(x):
    a, b, c = 1, 1, 0
    while (c <= x):
        c = a + b
        print(a, ' + ', b, ' = ', c)
        a = b
        b = c
        
#guess the number from 1 to 100 to win 
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

#rock paper scissor game
def rock_paper_scissor():

    import random
    run = 1
    while run:
        a = int(input('_____________________\n|enter 0 for rock   |\n|                   |\n|enter 1 for paper  |\n|                   |\n|enter 2 for scissor|\n|___________________|\n :- '))
        l = ['Rock','Paper','Scissor']
        b = random.choice(l)
        a = l[a]

        if a == 'Rock' and b == 'scissor' :
            print(f'win machine entered {b}')
        elif a == 'Paper' and b == 'Rock' :
            print(f'win machine entered {b}')
        elif a == 'Scissor' and b == 'Paper' :
            print(f'Win machine entered {b}')
        else: 
            print(f'lose machine entered {b}')

        run = int(input('enter 1 to continue and 0 to stop'))  
        
        
#password generator 8 characters
def password_gen8():
    import random
    charecters_list = [f'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','$','@','!','*','%','&'
                   ]
    password = ''
    for i in range(8):
        password += random.choice(charecters_list)
    print(f'you password is :- {password}')
