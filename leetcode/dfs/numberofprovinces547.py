from typing import *


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not any(isConnected):
            return 0
        else:
            # initialize all cells to be not visited
            rows = cols = len(isConnected)
            visited = set()
            regions = 0

            for row in range(rows):
                for col in range(cols):
                    if isConnected[row][col] == 1 and row not in visited:
                        self.explore(row, visited, isConnected)
                        regions += 1

            return regions


    def explore(self, row, visited, isConnected):
        # if its visited, then don't recurse/explore
        if row in visited:
            return
        else:
            visited.add(row)
            for col in range(len(isConnected)):
                if isConnected[row][col] == 1:
                    # these two cells are connected, lets explore again
                    self.explore(col, visited, isConnected)


# Test Cases

sol = Solution()

assert sol.findCircleNum([[]]) == 0
assert sol.findCircleNum([[1]]) == 1
assert sol.findCircleNum([[1,1]]) == 1
assert sol.findCircleNum([[1,0],[0,1]]) == 2
assert sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
assert sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3
