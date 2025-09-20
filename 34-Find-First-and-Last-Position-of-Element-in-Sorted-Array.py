class Solution:
    def searchRange(self, nums, target):
        def findFirst(arr, target):
            start, end = 0, len(arr) - 1
            first = -1
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] == target:
                    first = mid
                    end = mid - 1
                elif arr[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return first

        def findLast(arr, target):
            start, end = 0, len(arr) - 1
            last = -1
            while start <= end:
                mid = (start + end) // 2
                if arr[mid] == target:
                    last = mid
                    start = mid + 1
                elif arr[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return last

        return [findFirst(nums, target), findLast(nums, target)]
