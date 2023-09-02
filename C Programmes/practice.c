#include <stdio.h>

void revarr(int arr[], int n);
void fibonacci(int x);
int factorial(int nu);
int prime_num(int num);
int reverseInteger(int num);
int grade_check(int percentage);

int main()
{
    // u can use reverseinteger fn and prime number checker to make a twisted prime checker
    // welp try ok
    return 0;
}

// REVERSING ARRAY
void revarr(int arr[], int n)
{
    // REVERSING ARRAY
    for (int i = 0; i < n / 2; i++)
    {
        int first = arr[i];
        int second = arr[n - i - 1];
        arr[i] = second;
        arr[n - i - 1] = first;
    }
    // PRINTING UPDATED ARRAY
    for (int i = 0; i < n; i++)
    {
        printf("%d\t", arr[i]);
    }
};

// FIBONACCI SERIES
void fibonacci(int x)
{
    int a = 1, b = 1, c = 0, d = 0;
    while (d != x)
    {
        c = a + b;
        printf("\n%d + %d = %d", a, b, c);
        printf(" ");
        a = b;
        b = c;
        d++;
    };
};

// FACTORIAL BY RECURSION
int factorial(int nu)
{
    if (nu <= 1)
    {
        return 1;
    }
    else
    {
        return nu * factorial(nu - 1);
    }
};

// PRIME NUMBER CHECK
int prime_num(int num)
{
    int confirm = 0;
    printf("ENTER NUMBER :- ");
    scanf("%d", &num);
    for (int i = 2; i < num; i++)
    {
        if (num % i == 0)
        {
            confirm = 1;
            break;
        }
    }
    if (confirm == 0)
    {
        printf("%d is a prime number.\n", num);
    }
    else
    {
        printf("%d is not a prime number.\n", num);
    }
    return 0;
}

// REVERSING INTEGER
int reverseInteger(int num)
{
    int reversedNum = 0;
    while (num != 0)
    {
        reversedNum = (reversedNum * 10) + (num % 10);
        num /= 10;
    }
    return reversedNum;
}

// GRADE CHECKER
int grade_check(int percentage)
{
    if (percentage >= 60 && percentage <= 100)
    {
        printf("YOUR PERCENTAGE :- ");
        printf("%d \n", percentage);
        printf("YOUR GRADE IS A");
    }

    else if (percentage <= 50 && percentage > 60)
    {
        printf("YOUR PERCENTAGE :- ");
        printf("%d \n", percentage);
        printf("YOUR GRADE IS B");
    }

    else if (percentage <= 40 && percentage > 50)
    {
        printf("YOUR PERCENTAGE :- ");
        printf("%d \n", percentage);
        printf("YOUR GRADE IS C");
    }

    else if (percentage < 40)
    {
        printf("YOUR PERCENTAGE :- ");
        printf("%d \n", percentage);
        printf("YOUR GRADE IS FAIL");
    }

    else
    {
        printf("PLEASE PUT PERCENTAGE BETEN 1 - 100");
    }
}