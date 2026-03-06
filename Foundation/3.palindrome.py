class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x_copy = x
        rev = 0

        while x > 0:
            rem = x % 10              # extract last digit
            rev = rev * 10 + rem      # build reversed number
            x //= 10                  # remove last digit

        return rev == x_copy


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))   # True
    print(s.isPalindrome(-121))  # False
    print(s.isPalindrome(10))    # False
    print(s.isPalindrome(12321)) # True
