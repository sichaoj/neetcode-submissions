class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        zero_cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt += 1
            else:
                temp.append(nums[i])

        temp = temp + [0] * zero_cnt

        for j in range(len(nums)):
            nums[j] = temp[j]

        