def get_factorial(n):
    if n == 1:
        return n
    else:
        return n * get_factorial(n-1)

if __name__ == "__main__":
    n = 5
    print(get_factorial(n))