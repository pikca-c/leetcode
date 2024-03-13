class Solution(object):
    def maximumWealth(self, accounts):
        wealth = []
        for i in range(len(accounts)):
            wealth.append(int(sum(accounts[i])))
        return max(wealth)

  #26ms runtime, beats 94%
