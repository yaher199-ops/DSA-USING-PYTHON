class Solution(object):
    def peakIndexInMountainArray(self, arr):
        start=1
        end=len(arr)-2

        while start<=end:
            mid=(start+end)//2

            if arr[mid-1]<arr[mid]and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]<arr[mid]:
                start=mid+1
            else:
                end=mid-1
        return -1
arr=[1,3,5,7,4,2,0]
c1=Solution()
print("the peak element is: ",c1.peakIndexInMountainArray(arr))