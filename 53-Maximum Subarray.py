class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum + nums[i] > nums[i]:
                current_sum = current_sum + nums[i]
            else:
                current_sum = nums[i]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s1 = Solution()
result = s1.maxSubArray(nums)
print("Maximum Subarray Sum:", result)
