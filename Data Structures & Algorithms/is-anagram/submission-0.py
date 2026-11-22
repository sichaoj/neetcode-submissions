class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted([i for i in s])
        t_list = sorted([i for i in t])

        if s_list == t_list:
            return True
        else:
            return False
