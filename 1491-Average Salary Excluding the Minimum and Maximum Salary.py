class Solution(object):
    def average(self, salary):
        return(float((sum(salary)-max(salary)-min(salary)))/float((len(salary)-2)))

        """
        :type salary: List[int]
        :rtype: float
        """
        
