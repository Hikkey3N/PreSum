class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.preSum = [0] * len(nums)  # Create an array to store prefix sums
        if nums:
            self.preSum[0] = nums[0]  # The first element is just nums[0]
            for indx in range(1, len(nums)):
                self.preSum[indx] = nums[indx] + self.preSum[indx - 1]  # Compute prefix sum   

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.preSum[right]
        else:
            return self.preSum[right] - self.preSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)