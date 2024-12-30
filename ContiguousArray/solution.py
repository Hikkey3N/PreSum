class Solution(object):
    def findMaxLength(self, nums):
        sum_index_map = {0: -1}  # Initialize with sum 0 at index -1
        max_length = 0
        cumulative_sum = 0
        
        for indx in range(len(nums)):
            # Update the cumulative sum
            if nums[indx] == 0:
                cumulative_sum -= 1  # Treat 0 as -1
            else:
                cumulative_sum += 1
            
            # Check if cumulative_sum has been seen before
            if cumulative_sum in sum_index_map:
                # Calculate the length of the subarray
                subarray_length = indx - sum_index_map[cumulative_sum]
                max_length = max(max_length, subarray_length)
            else:
                # Store the first occurrence of cumulative_sum
                sum_index_map[cumulative_sum] = indx
        
        return max_length

# O(n) time complexity