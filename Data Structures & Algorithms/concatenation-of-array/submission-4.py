class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [None] * (2*n)
        # print(2*n)

        for i in range(n):
            ans[i] = ans[i+n] = nums[i]
            # ans[i+n] = nums[i]

        return ans

        '''
        time complexity: O(n)
        - where n is the length of the input array
        - iterate through input once, performs 2n writes to output array

        space complexity: O(n)
        - allocates array of size 2n to write outputs
        '''