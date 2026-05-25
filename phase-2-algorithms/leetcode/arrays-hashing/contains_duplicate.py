from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1, 2, 3, 1]))
    print(sol.hasDuplicate([1, 2, 3, 4]))
