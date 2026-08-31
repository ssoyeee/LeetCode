class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x<0
        x = abs(x)

        reversed_integer = 0 
        while x > 0:
            last_digit = x % 10
            reversed_integer = reversed_integer * 10 + last_digit
            x = x // 10
        
        if is_negative:
            return -reversed_integer
        return reversed_integer