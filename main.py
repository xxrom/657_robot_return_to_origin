class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # print('moves', moves)
        vertical = 0
        horizontal = 0

        for char in moves:
            if char == "L":
                horizontal += 1
            if char == "U":
                vertical += 1
            if char == "R":
                horizontal -= 1
            if char == "D":
                vertical -= 1

        print('H %d, V %d' % (horizontal, vertical))

        # if each side in sum by lines gets zero (0),
        # then robot retruns on start postion
        return horizontal == 0 and vertical == 0


my = Solution()

moves0 = "LUURD"
moves1 = "LURD"

ans = my.judgeCircle(moves1)
print("ans", ans)
