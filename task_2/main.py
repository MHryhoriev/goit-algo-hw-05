def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    count_steps = 0
 
    while low <= high:
        count_steps += 1
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
           return (count_steps, arr[mid])
        
    upper_bound = None

    if low < len(arr):
        upper_bound = arr[low]
    else:
        upper_bound = float('inf')

    return (count_steps, upper_bound)


def main():
    sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5]
    value_to_find = 3.5
    result = binary_search(sorted_array, value_to_find)
    print(result)

if __name__ == "__main__":
    main()