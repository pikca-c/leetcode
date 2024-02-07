#I did not come up with this solution. I initially tried to break it by using multiple loops but that method was taking way too long. This is a much more sophisicated solution.
class Solution(object):
    def repeatedSubstringPattern(self, s):
        s_fold = "".join((s[1:],s[:-1]))
        return s in s_fold
