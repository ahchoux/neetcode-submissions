class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_len = len(nums)
        set_len = len(list(set(nums)))

        return (nums_len != set_len)
        # counter = {}

        # n = len(nums)
        # for i in range(n):
        #     if (nums[i] not in counter):
        #         num = nums[i]
        #         counter[num] = 1
        #     else: 
        #         return True
        
        # print(counter)
        # return False
        