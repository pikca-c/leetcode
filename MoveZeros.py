#Final submission
def moveZeroes(self, nums):
        count = 0
        rtrn = []
        for i in range(len(nums)):
            if nums[i] == 0:
                count = count + 1
                nums.append(0)
        for i in range(count):
            nums.remove(0)
        return nums
#Initial idea
def moveZeroes(nums):
        count = 0
        rtrn = []
        for i in range(len(nums)):
            if nums[i] == 0:
                count = count + 1
            elif nums[i] != 0: 
                rtrn.append(nums[i])
        print(count)
        for i in range(count):
            rtrn.append(0)
        return rtrn

print(moveZeroes([0,1,0,3,12]))
