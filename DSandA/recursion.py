# Fibonacci

def get_fib_loop(position):
    if position == 0: return 0
    if position == 1: return 1

    first = 0
    second = 1
    next = first + second
  
    for i in range(2, position):
        first = second
        second = next
        next = first + second   
    return next

print(get_fib_loop(7))

def get_fib_recursive(input):
    if input <= 1:
        return input
    else:
        output = get_fib_recursive(input - 1) + get_fib_recursive(input - 2)
        return output
    
print(get_fib_recursive(7))

def get_fib_recursion(position):
    if position == 0 or position == 1:
        return position
    return get_fib_recursion(position - 1) + get_fib_recursion(position - 2)



print(get_fib_recursion(7))

# Factorial

def factorial_loop(n):
    output = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            output = output * i
            print(i , output)
        return output

print(factorial_loop(7))          # 5040


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(7))       # 5040
