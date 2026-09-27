class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec_cnt = 0
        max_consec = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                consec_cnt += 1 
                if consec_cnt > max_consec:
                    max_consec = consec_cnt 
                else:
                    max_consec
            else:
                consec_cnt = 0

        return max_consec

       
        