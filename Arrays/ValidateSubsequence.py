def issubsequence(nums, arr):
    extra=[]
    for i in range(len(nums)):
        if nums[i] in arr:
            extra.append(nums[i])
    if len(extra) == len(nums):
        return True
    else:
        return False;

arr=[5,1,22,25,6,-1,8,10]
nums=[1,6,-1,10]

print(issubsequence(nums,arr))