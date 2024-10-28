def fibonacci_list(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

print("\nFibonacci List up to 10:")
print(fibonacci_list(10))

def index_of_first_exceeding(value):
    a, b, index = 0, 1, 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index

value = 20
print(f"\nThe index of the first Fibonacci number that exceeds {value} is {index_of_first_exceeding(value)}.")


def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

test_num = 21
print(f"\nIs {test_num} a Fibonacci number? {is_fibonacci(test_num)}")

def fibonacci_ratios(limit):
    ratios = []
    a, b = 0, 1
    for _ in range(2, limit):
        a, b = b, a + b
        ratios.append(b / a if a != 0 else None)
    return ratios

ratios = fibonacci_ratios(15)
print("\nRatios of consecutive Fibonacci numbers:")
print(ratios)