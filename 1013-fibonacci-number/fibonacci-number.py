class Solution:
    def fib(self, n: int) -> int:

        def fibbo(n):
            if n == 0:
                return 0
            if n == 1:
                return 1

            return fibbo(n - 1) + fibbo(n - 2)

        return fibbo(n)
        