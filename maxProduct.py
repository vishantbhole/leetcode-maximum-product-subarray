class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        curMax = 1
        curMin = 1
        j = 0
        for num  in nums:
            if(num == 0):
                curMax = 1
                curMin = 1
            tmp = curMax * num
            curMax = max(num * curMax ,num * curMin, num)
            curMin = min(tmp ,num * curMin, num)
            res = max(res,curMax)
        return res

        
        
