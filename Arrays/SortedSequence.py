def sorted_squared_array(array):
    n = len(array)
    result = [0] * n
    left, right = 0, n - 1
    idx = n - 1

    while left <= right:
        left_square = array[left] ** 2
        right_square = array[right] ** 2

        if left_square > right_square:
            result[idx] = left_square
            left += 1
        else:
            result[idx] = right_square
            right -= 1

        idx -= 1

    return result

# Example usage:
input_array = [-4, 2, 0, 3, -5]
result = sorted_squared_array(input_array)
print("Sorted squared array:", result)
