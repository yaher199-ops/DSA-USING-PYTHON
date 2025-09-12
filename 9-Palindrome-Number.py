class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        num_str = str(x)
        reversed_str = num_str[::-1]

        return num_str == reversed_str


c1 = Solution()
print(c1.isPalindrome(121))
print(c1.isPalindrome(-121))
print(c1.isPalindrome(10))
