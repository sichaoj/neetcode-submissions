class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for num in nums:
            if num not in cnt.keys():
                cnt[num] = 1
            else:
                cnt[num] += 1
        
        if len(cnt) == 0:
            return False
        elif max(cnt.values()) > 1:
            return True
        else:
            return False



        