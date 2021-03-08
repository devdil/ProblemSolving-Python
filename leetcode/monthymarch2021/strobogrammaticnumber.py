"""
Problem Link: https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3664/
"""
class Solution:

    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammaticnumbers = {'6': '9', '9': '6', '8': '8', '1': '1'}

        left = 0
        right = len(num) - 1

        while left <= right:

            # if number not in map, return false right away
            if num[right] not in strobogrammaticnumbers:
                return False

            else:
                # check if its a mirror image, then increment two pointers accordingly
                if num[left] == strobogrammaticnumbers.get(num[right]):
                    left += 1
                    right -= 1
                else:
                    # else return false right away
                    return False

        return True


sol = Solution()
sol.isStrobogrammatic("2")
