class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n < 1 or n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfTwo(1))    # True (2^0)
    print(s.isPowerOfTwo(2))    # True (2^1)
    print(s.isPowerOfTwo(16))   # True (2^4)
    print(s.isPowerOfTwo(12))   # False
    print(s.isPowerOfTwo(0))    # False
    print(s.isPowerOfTwo(-2))   # False
