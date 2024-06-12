def twosum(arr, targetsum):
    nums = []  # Use a list to store encountered numbers
    for num in arr:
        ans = targetsum - num
        if ans in nums:
            return [ans, num]
        else:
            nums.append(num)  # Add the current number to the list
    return []

arr = [3, 5, -4, 8, 11, 1, -1, 6]
targetsum = 10

print(twosum(arr, targetsum))
