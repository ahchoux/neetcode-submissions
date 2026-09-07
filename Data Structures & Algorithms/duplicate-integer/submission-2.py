class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)
        ans = set()
        nums.sort()

        for i, num in enumerate(nums):
            if (num in ans):
                return True
            ans.add(num)

        return False

        # nums_len = len(nums)
        # set_len = len(list(set(nums)))

        # return (nums_len != set_len)
