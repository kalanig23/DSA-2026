class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start=0
        end=len(numbers)-1
        while(start<end):
            sum=numbers[start]+numbers[end]
            if(sum==target):
            #question mee plus one karne ko bola hai isliye plus on kiya hai return ke timee paar
            #Return the indices of the two numbers, index1 and index2, added by one as an 
            #integer array [index1, index2] of length 2.
                return [start+1,end+1]
            elif(sum>target):
                end=end-1
            else:
                start=start+1
        return [-1,-1]
                


        
