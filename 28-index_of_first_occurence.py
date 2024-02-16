class Solution(object):
    def strStr(self, haystack, needle):
        x = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i:i+x]:
                return i
        return -1
            
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
