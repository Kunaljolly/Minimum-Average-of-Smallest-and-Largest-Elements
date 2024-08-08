class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages = []
        while(len(nums)!=0):
            averages.append((nums[0]+nums[-1])/2)
            nums.remove(nums[0])
            nums.remove(nums[-1])
        return min(averages)
