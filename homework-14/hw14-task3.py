def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def main():

    fib_gen = fibonacci_generator(10)
    print("First 10 Fibonacci numbers:")
    for fib in fib_gen:
        print(fib, end=" ")
    print()

    fib_gen = fibonacci_generator(5)
    print("First 5 Fibonacci numbers:")
    for fib in fib_gen:
        print(fib, end=" ")
    print()

    fib_gen = fibonacci_generator(15)
    print("First 15 Fibonacci numbers:")
    for fib in fib_gen:
        print(fib, end=" ")
    print()

main()
