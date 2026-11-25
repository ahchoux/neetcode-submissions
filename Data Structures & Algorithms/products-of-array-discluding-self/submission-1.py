class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # prefix / suffix
        n = len(nums)
        output = [1] * n
        prefix = 1
        suffix = 1

        # first pass prefix
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        for j in range(n-1, -1, -1):
            output[j] = output[j] * suffix
            suffix *= nums[j]

        return output
 

        # # brute force O(n^2)
        # n = len(nums)
        # output = [1] * n
        # print(output)
        
        # for i in range(n):
        #     for j in range(n):
        #         if (j != i):
        #             output[j] = output[j] * nums[i]

        # return output

