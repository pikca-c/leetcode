#Initial idea, a variation of the same code submitted to codewars
class Solution(object):
    def romanToInt(self, s):
        rom = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        num = [1000, 500, 100, 50, 10, 5, 1]
        result = 0
        for index, value in enumerate(s):
            first_num = num[rom.index(value)]
            second_num = num[rom.index(s[index+1])]if index+1 != len(s) else -1
            if first_num >= second_num: result += first_num
            else: result -= first_num
            
        return result

#Best solution found:
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
#How my code can be improved: Use simplier methods e.g. are there any ways to decrease the complexity of the question, by using a single loop
#and no if else statements the program can be much quicker
