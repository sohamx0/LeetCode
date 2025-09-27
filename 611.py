# Valid Triangle Number

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        k = 0
        for c in range(n - 1, 1, -1):
            a, b = 0, c - 1
            while a != b:
                if nums[a] + nums[b] > nums[c]:
                    k += (b - a)
                    b -= 1
                else:
                    a += 1
        return k
    

print(Solution().triangleNumber([2,2,3,4]))