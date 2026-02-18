class Solution:
    def fib(self, n: int) -> int:

        # using basic for loop

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        f = [0] * (n + 1)
        f[0] = 0
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]

        # recursion

        def fibbo(n):
            if n <= 1:
                return n

            last = fibbo(n - 1)
            slast = fibbo(n - 2)
            return last + slast

        return fibbo(n)

       
        