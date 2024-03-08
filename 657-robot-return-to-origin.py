#initial idea
class Solution(object):
    def judgeCircle(self, moves):
        x = 0
        y = 0
        moves = list(moves)
        for i in range(len(moves)):
            if moves[i] == "L":
                x -= 1
            elif moves[i] == "R":
                x += 1
            elif moves[i] == "U":
                y += 1
            elif moves[i] == "D":
                y -= 1
        if x==0 and y==0: return True
#this solution is incredibly slow (50ms runtime & only beats 40% of users)
#alternative (much quicker) solution after a thinking a bit:
class Solution(object):
    def judgeCircle(self, moves):
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")

        """
        :type moves: str
        :rtype: bool
        """
#11ms runtime, beats 98%
