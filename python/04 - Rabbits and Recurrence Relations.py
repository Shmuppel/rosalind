from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_rabbits(n, k):
    """
    Prints the total number of rabbit pairs after n months, given that each pair
    produces k offspring pairs, and each offspring takes 1 month to mature.
    :param n: total months to breed rabbits for.
    :param k: total offspring pairs per rabbit pair produced per month
    :return: Fibonacci-esque recursion
    """
    if n <= 1:
        return n  # Returning n is crucial so fib_rab(n-2, k) * k returns 0 on n = 2

    print(f'Month {n}:',
          f1 := fibonacci_rabbits(n-1, k),
          f2 := fibonacci_rabbits(n-2, k) * k,
          f1 + f2)

    return f1 + f2


print(fibonacci_rabbits(5, 3))
