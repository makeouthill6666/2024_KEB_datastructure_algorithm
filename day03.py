def fibo_recursion(number:int) -> int:
    """
    fibonacci function by recursion.
    :param number: integer number
    :return: integer number
    """
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibo_recursion(number-1) + fibo_recursion(number-2)


def fibo_repetition(number:int) -> int:
    """
    fibonacci function by repetition.
    :param number: integer number
    :return: integer number
    """
    a = 0
    b = 1
    for _ in range(number):
        # a = b
        # b = a + b
        a, b = b, a + b
    return a


memo = [None for _ in range(100)]

def fibo_memoization(n:int, memo:list) -> int:
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """

    if memo[n] is not None:
        return memo[n]
    if n < 2:
        result = n
    else :
        result = fibo_memoization(n-1, memo) + fibo_memoization(n-2, memo)
        memo[n]=result
    return result

n = int(input("Input number : "))
for i in range(0, n):
    print(i)
    print(fibo_memoization(i, memo))

