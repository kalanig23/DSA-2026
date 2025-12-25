import math
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = self.firstPosition(nums, target)
        last = self.lastPosition(nums, target)
        return [first, last]

    def firstPosition(self, nums, target):
        start=0
        end=len(nums)-1
        fp=-1
        
        while(start<=end):
            mid=(start+(end-start)//2)
            if(nums[mid]==target):
                fp=mid
                end=mid-1
            elif(nums[mid]<target):
                start=mid+1
            else:
                end=mid-1
        return fp
    
    def lastPosition(self, nums, target):
        start=0
        end=len(nums)-1
        lp=-1
        while(start<=end):
            mid=(start+(end-start)//2)
            if(nums[mid]==target):
                lp=mid
                start=mid+1
            elif(nums[mid]<target):
                start=mid+1
            else:
                end=mid-1
        return lp
