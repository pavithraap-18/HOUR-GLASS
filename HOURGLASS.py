def hourglassSum(arr):
    max_sum = -float('inf')  # Initialize to a very small number
    
    for i in range(4):  # Rows (top-left corner of hourglass)
        for j in range(4):  # Columns (top-left corner of hourglass)
            # Calculate sum of the hourglass
            hourglass = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +  # Top row
                arr[i+1][j+1] +  # Middle element
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]  # Bottom row
            )
            max_sum = max(max_sum, hourglass)  # Update max_sum if needed

    return max_sum

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = hourglassSum(arr)
    print(result)
