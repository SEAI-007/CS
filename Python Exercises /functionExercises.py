# 1. Sum of List Elements
def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    print(sum)
    return(sum)
    
sum_list([1,2,3,4,5])

# 2. Sum of List Elements
def repeat_greeting(name,times):
    for time in range(0,times):
        print(f"Hallo {name}")

repeat_greeting("Efecan",0)

# 3. Factorial Calculation
def factorial(n):
    if n > 0 and isinstance(n, int):
        factorial = 1
        while n != 0 and n>0:
            factorial *= n
            n -= 1
        print(factorial)
        return(factorial)
    else:
        print("Please input a positive integer")

factorial(7)

# 4. Fibonacci Sequence Generator
# def fibonacci(n):
#     for i in range(0,n):


# fibonacci(5)

# 5. Maximum of Two Numbers
def max_of_two(a,b):
    if a > b:
        print(a)
        return a
    elif a == b:
        print("Both are equal")
    else:
        print(b)
        return(b)

max_of_two(5,10)

# 6. Print a Pattern with Nested Loops
def print_triangle(rows):
    for row in range(0,rows+1):
        print("*"*row)

print_triangle(3)

