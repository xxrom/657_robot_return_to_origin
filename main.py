class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # print('moves', moves)
        left = 0
        right = 0
        up = 0
        down = 0

        for char in moves:
            if char == "L":
                left += 1
            if char == "U":
                up += 1
            if char == "R":
                right += 1
            if char == "D":
                down += 1

        # print('L %d, U %d, R %d, D %d' % (left,  up, right, down))

        # if each side in sum by lines gets zero (0),
        # then robot retruns on start postion
        return (left - right) == 0 and (up - down) == 0


my = Solution()

moves0 = "LUURD"
moves1 = "LURD"

ans = my.judgeCircle(moves1)
print("ans", ans)
