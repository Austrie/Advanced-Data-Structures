def fib(n):
    if (n is 0 or n is 1):
        return 1

    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print("Im here")
    print(fib(50))
