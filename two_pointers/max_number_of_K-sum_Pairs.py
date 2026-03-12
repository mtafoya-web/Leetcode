### Optimal Algorithm Using Hashmap O(n) time####
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = dict()
        count = 0
        for num in nums:
            compl = k - num
            if compl in seen and seen[compl] > 0:
                count += 1
                seen[compl] -= 1
            elif num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        return count 
            
            