class Solution(object):
    def search(self, nums, target):
        start=0
        end=len(nums)-1

        while start<=end:
            mid=(start+end)//2
            if target>nums[mid]:
                start=mid+1
            elif target<nums[mid]:
                end=mid-1
            else:
                return mid
        return -1
arr=[1,2,3,4,5,6,7,8,9,10]
target=3
s1=Solution()
position=s1.search(arr,target)
if position!=-1:
    print("element found at index:",position)
else:
    print("element not found ")