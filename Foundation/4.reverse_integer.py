class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        n = abs(x)

        while n != 0:
            last = n % 10          # extract last digit
            rev = rev * 10 + last  # build reversed number
            n //= 10               # remove last digit

        # A 32-bit signed integer has a range from −2**31 to 2**31 - 1
        if rev > 2**31 - 1:
            return 0

        return -rev if x < 0 else rev


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))        # 321
    print(s.reverse(-123))       # -321
    print(s.reverse(120))        # 21
    print(s.reverse(1534236469)) # 0 (overflow case)
