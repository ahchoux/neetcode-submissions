class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        counter = {}

        n = len(nums)
        for i in range(n):
            if (nums[i] not in counter):
                num = nums[i]
                counter[num] = 1
            else: 
                return True
        
        print(counter)
        return False
        