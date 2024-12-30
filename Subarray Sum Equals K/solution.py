class Solution(object):
    def subarraySum(self, nums, k):
        preSumCount = {0: 1}  # Hashset
        preSum = 0
        count = 0

        for num in nums:
            preSum += num

            # Updating count if the requirement is met
            if preSum - k in preSumCount:
                count += preSumCount[preSum - k]

            # Updating the hashset
            if preSum in preSumCount:
                preSumCount[preSum] += 1
            else:
                preSumCount[preSum] = 1
        
        return count

# O(n)