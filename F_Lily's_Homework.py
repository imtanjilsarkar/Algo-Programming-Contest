def lilysHomework(arr):
    n = len(arr)
    
    # Create sorted versions
    sorted_asc = sorted(arr)
    sorted_desc = sorted(arr, reverse=True)
    
    # Count swaps for ascending order
    arr_copy = arr.copy()
    pos_dict = {}
    for i, num in enumerate(sorted_asc):
        pos_dict[num] = i
    
    swaps_asc = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i] and arr_copy[i] != sorted_asc[i]:
            cycle_size = 0
            j = i
            
            while not visited[j]:
                visited[j] = True
                j = pos_dict[arr_copy[j]]
                cycle_size += 1
            
            swaps_asc += (cycle_size - 1)
    
    # Count swaps for descending order
    arr_copy = arr.copy()
    pos_dict = {}
    for i, num in enumerate(sorted_desc):
        pos_dict[num] = i
    
    swaps_desc = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i] and arr_copy[i] != sorted_desc[i]:
            cycle_size = 0
            j = i
            
            while not visited[j]:
                visited[j] = True
                j = pos_dict[arr_copy[j]]
                cycle_size += 1
            
            swaps_desc += (cycle_size - 1)
    
    return min(swaps_asc, swaps_desc)

# Read input (same as your previous problems)
n = int(input())
arr = list(map(int, input().split()))

# Calculate result
result = lilysHomework(arr)
print(result)