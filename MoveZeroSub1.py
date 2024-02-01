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
