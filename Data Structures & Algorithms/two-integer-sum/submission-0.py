class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        differences = {}

        if (n <= 2):
            return [0, 1]

        # nums[i] = target - nums[j]
        for i in range(n):
            diff = target - nums[i]
            if (diff in differences):
                return [differences[diff], i]
            else:
                differences[nums[i]] = i 
