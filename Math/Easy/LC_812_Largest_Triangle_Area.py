# Problem: https://leetcode.com/problems/largest-triangle-area/
# Approach: Brute-force all triplets and compute area using the shoelace formula.
# Track the maximum area found.
# Time: O(n^3) | Space: O(1)

# Largest Triangle Area

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        n = len(points)
        A = 0
    
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                
                    area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0
                    A = max(A, area)
    
        return A

print(Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
