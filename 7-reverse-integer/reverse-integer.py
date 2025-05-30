class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_x = int(str(x_abs)[::-1])
        result = sign * reversed_x
        if -2**31 <= result <= 2**31 - 1:
            return result
        else:
            return 0
