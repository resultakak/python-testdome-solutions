from functools import lru_cache

class Problem:

    @staticmethod
    @lru_cache(2 ** 16)
    def fibonacci(n):
        if n < 0:
            return 0
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return Problem.fibonacci(n - 1) + Problem.fibonacci(n - 2)

print(Problem.fibonacci(6))
