#include <stdio.h>

int Factorial(int num);
int Gcd(int num1, int num2);
int Fibonacci(int num);
void Fibonacci_till_a(int a);

int main()
{
    //----Factorial----
    printf("--------FACTORIAL--------\n");
    printf("\n");
    int num;
    printf("Enter the number :- ");
    scanf("%d", &num);
    int factorial = Factorial(num);
    printf("Factorial of %d is %d\n", num, factorial);

    //----Gcd | Hcf----
    printf("\n");
    printf("--------GCD--------\n");
    printf("\n");
    int num1;
    int num2;
    printf("Enter First number :- ");
    scanf("%d", &num1);
    printf("Enter Second number :- ");
    scanf("%d", &num2);
    int Hcf = Gcd(num1, num2);
    printf("Gcd of %d and %d is %d \n", num1, num2, Hcf);

    //----Fibonacci Series----
    printf("\n");
    printf("--------Fibonacci Series--------\n");
    printf("\n");
    int a;
    printf("Enter nth number for fibonacci series :- ");
    scanf("%d", &a);
    Fibonacci_till_a(a);
    return 0;
}

// Factorial By Recursion
int Factorial(int num)
{
    if (num == 0)
    {
        return 1;
    }
    else
    {
        return num * Factorial(num - 1);
    }
}

// Gcd(Greatest Common Factor) by recursion
int Gcd(int num1, int num2)
{
    if (num1 == 1 && num2 == 1)
    {
        return 1;
    }
    else if (num1 == num2)
    {
        return num1;
    }
    else if (num1 > num2)
    {
        Gcd(num1 - num2, num2);
    }
    else
    {
        Gcd(num1, num2 - num1);
    }
}

// function for getting numth value of fibonacci series With recursion
int Fibonacci(int num)
{
    if (num == 0)
    {
        return 0;
    }
    else if (num == 1)
    {
        return 1;
    }
    else
    {
        return Fibonacci(num - 1) + Fibonacci(num - 2);
    }
}

// for printing the fibonacci series
void Fibonacci_till_a(int a)
{
    for (int i = 0; i <= a; i++)
    {
        int result = Fibonacci(i);
        printf("%dth Value -> %d \n", i, result);
    }
}