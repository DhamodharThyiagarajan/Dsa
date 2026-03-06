class Solution:
    def secondHighest(self, s):
       
        digits = []
        for ch in s :
            if '0' <= ch <= '9':
              digits.append(int(ch))
       
        if len(digits) < 2:
            return -1

        first = float('-inf')
        second = float('-inf')

        for num in digits:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num

        return second if second != float('-inf') else -1

if __name__ == "__main__":
    sol = Solution()
    # Test cases
    print(sol.secondHighest("abc123"))  # Output: 2
    print(sol.secondHighest("a1b2c3d4"))  # Output: 3
    print(sol.secondHighest("abc"))  # Output: -1
