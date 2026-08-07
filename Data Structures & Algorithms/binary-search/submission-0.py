class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:

            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif target<nums[mid]:
                high = high -1
            elif target>nums[mid]:
                low = low +1
        if low > high:
            return -1