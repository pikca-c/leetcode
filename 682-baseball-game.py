class Solution(object):
    def calPoints(self, operations):
        total = []
        for i in range(len(operations)):
            if operations[i] == "C":
                total.pop(-1)
            elif operations[i] == "D":
                total.append(total[-1]*2)
            elif operations[i] == "+":
                total.append(int(total[-1]+total[-2]))
            else: total.append(int(operations[i]))
        return(sum(total))
#As far as I am aware this is the best solution that does not require a lot of time to solve
