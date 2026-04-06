class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0

        for i in range(len(s) - 1):
            total += abs(ord(s[i + 1]) - ord(s[i]))

        return total


sol = Solution()
print(sol.scoreOfString("code"))     # 24
print(sol.scoreOfString("neetcode")) # 65