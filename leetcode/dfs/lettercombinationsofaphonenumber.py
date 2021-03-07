"""
Problem solution link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        else:
            answer = []
            tmp_result = []
            digit_letter_map = {

                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
            }

            self.exploreAllCombinations(answer, tmp_result, digits, digit_letter_map, 0)
            return answer
    """
        For each index in the digits, gets all the possible alphabets for that digit
        and then calls the function again with the next index. Once we run out of characters
        or gone past the index, we can store them in answer and continue. After the function
        has returned we mmust remove the last character inserted to ensure the consistency of the next
        exploration
    """
    def exploreAllCombinations(self, answer, tmp_result, digits, digit_letter_map, current_index):
        if current_index >= len(digits):
            combination = "".join(tmp_result)
            answer.append(combination)
            return
        else:
            for letter in digit_letter_map.get(digits[current_index]):
                tmp_result.append(letter)
                self.exploreAllCombinations(answer, tmp_result, digits, digit_letter_map, current_index+1)
                tmp_result.pop(-1)


sol = Solution()
#test1
assert sol.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# test 2
assert sol.letterCombinations(None) == []

