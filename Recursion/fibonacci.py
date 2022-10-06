import time

def get_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)

fibonacci_store = dict()
def get_fibonacci_dynamic(n):
    if n == 1 or n == 2:
        return 1
    else:
        if str(n-1) in fibonacci_store.keys():
            n_minus_one = fibonacci_store[str(n-1)]
        else:
            n_minus_one = get_fibonacci_dynamic(n-1)
            fibonacci_store[str(n-1)] = n_minus_one

        if str(n-2) in fibonacci_store.keys():
            n_minus_two = fibonacci_store[str(n-2)]
        else:
            n_minus_two = get_fibonacci_dynamic(n-2)
            fibonacci_store[str(n-2)] = n_minus_two
        return n_minus_one + n_minus_two

if __name__ == "__main__":
    n = 35

    start_time = time.time()
    print(get_fibonacci(n))
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print(get_fibonacci_dynamic(n))
    print("--- %s seconds ---" % (time.time() - start_time))