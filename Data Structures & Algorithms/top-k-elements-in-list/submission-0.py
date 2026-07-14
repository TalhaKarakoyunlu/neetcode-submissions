class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_to_freq_dict = Counter(nums)

        buckets = [[] for x in range(len(nums) + 1)]
        
        for num, freq in num_to_freq_dict.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        

