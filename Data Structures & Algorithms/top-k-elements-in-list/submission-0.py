import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 1. create dict (key=unique num, value=occurence) 
        occ = {}
        for num in nums:
            occ[num] = 1 + occ.get(num, 0)

        heap = []
        # 2. heapify on dict.values()
        for num, freq in occ.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

"""
        # 3. pop heapq k times and return list of indices
        for i in range(k):
            heapq.heappop()
        # sorted_nums = list(set(sorted(nums, reverse=True))) # nlogn
        # print(f"sorted setlist: {sorted_nums}")
        # return sorted_nums[:k]
        """

        