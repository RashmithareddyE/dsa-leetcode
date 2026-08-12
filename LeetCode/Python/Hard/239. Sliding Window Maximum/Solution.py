class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        ans = []

        for right in range(len(nums)):
            if right - left + 1 == k:
                m = nums[left:right + 1]
                n = max(m)
                ans.append(n)
                left += 1

        return ans