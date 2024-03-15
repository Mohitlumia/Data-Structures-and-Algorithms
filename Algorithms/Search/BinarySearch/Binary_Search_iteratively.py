

def binary_search(numbers_list, number_to_find):
    """
    iterative binary search has logarithmic time and constant space complexity.
    
    Time Complexity:    O(log n)
    Space Complexity:   O(1)
    """
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        # check if number_to_find is equals to mid_number
        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_number - 1
        
    # if number_to_find is not in number_list
    return -1



# sorted list of numbers
nums = [0,1,2,3,4,5,6,7,8,9]

# find index of number n in list
n = 3

index = binary_search(nums,n)

if index != -1:
    print("{} in numbers_list at index value {}".format(n,index))
else:
    print("{} is not in numbers_list".format(n))
