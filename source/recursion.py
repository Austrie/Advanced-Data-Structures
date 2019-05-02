#!python
import time

def fibonacci(n):
    """fibonacci(n) returns the n-th number in the Fibonacci sequence,
    which is defined with the recurrence relation:
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2), for n > 1"""
    # Check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('fibonacci is undefined for n = {!r}'.format(n))
    # Implement fibonacci_recursive, _memoized, and _dynamic below, then
    # change this to call your implementation to verify it passes all tests
    return fibonacci_recursive(n)
    # return fibonacci_memoized(n)
    # return fibonacci_dynamic(n)


def fibonacci_recursive(n):
    # Check if n is one of the base cases
    if n == 0 or n == 1:
        return n
    # Check if n is larger than the base cases
    elif n > 1:
        # Call function recursively and add the results together
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n):
    # This code was originally belief that fibonacci starts at '0' (e.g. fib(0) == 1, fib(2) == 2)
    # This code was changed so fibonacci starts at 1 (e.g. fib(0) == 0, fib(2) == 1)
    n = int(n) - 1
    if (n < 0):
        return 0
    return fibonacci_memoized_helper(n, {})
    # Once implemented, change fibonacci (above) to call fibonacci_memoized
    # to verify that your memoized implementation passes all test cases

def fibonacci_memoized_helper(n, htable):
    if n < 0:
        return 1
    if n in htable:
        return htable[n]
    if n == 0 or n == 1:
        htable[0] = 1
        htable[1] = 1
        return 1

    htable[n] = fibonacci_memoized_helper(n - 1, htable) + fibonacci_memoized_helper(n - 2, htable)
    return htable[n]


def fibonacci_dynamic(n):
    # This code was originally belief that fibonacci starts at '0' (e.g. fib(0) == 1, fib(2) == 2)
    # This code was changed so fibonacci starts at 1 (e.g. fib(0) == 0, fib(2) == 1)
    n = int(n) - 1
    if n < 0:
        return 0
    if (n == 0 or n == 1):
        return 1

    return fibonacci_dynamic_helper(n, 1, 1, 1)
    # Once implemented, change fibonacci (above) to call fibonacci_dynamic
    # to verify that your dynamic implementation passes all test cases

def fibonacci_dynamic_helper(n, curr, total, prev):
    # print("N " + str(n))
    # print("Curr " + str(curr))
    # print("Total " + str(total))
    # print("Prev " + str(prev))
    # print("_________")
    if curr == n:
        return total

    return fibonacci_dynamic_helper(n, curr + 1, (total + prev), total)





def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        start = time.time()
        result = fibonacci(num)
        end = time.time()
        print('fibonacci({}) => {}'.format(num, result))
        print("Time taken {}".format(end - start))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
