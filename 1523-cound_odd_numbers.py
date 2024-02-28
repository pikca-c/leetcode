class Solution(object):
    def countOdds(self, low, high):
        if low % 2 == 0:
            return(high-low+1)//2
        return (high-low)//2 + 1
#I originaly used a for loop and it timed out so this is another mathematical way that I went for
