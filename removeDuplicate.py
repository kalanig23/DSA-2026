class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        second=start+1
        count=1
        while(start<len(nums) and second>start and second<len(nums)):
            if(nums[second-1]==nums[second]):
                second=second+1
            else:
                start=start+1
                nums[start]=nums[second]
                second=second+1
                count=count+1
        return count









