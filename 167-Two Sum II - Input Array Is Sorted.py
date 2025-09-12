class Solution(object):
    def twoSum(self, arr, target):
        start = 0
        end = len(arr) - 1

        while start < end:
            pairsum = arr[start] + arr[end]

            if pairsum > target:
                end -= 1
            elif pairsum < target:
                start += 1
            else:
                return [start + 1, end + 1]

        return []


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11
c1 = Solution()
result = c1.twoSum(arr, target)

print("Pair sum are:", result)
