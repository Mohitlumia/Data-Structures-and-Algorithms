

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if left_index > right_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index
    
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_number - 1
    
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


# sorted list of numbers
nums = [0,1,2,3,4,5,6,7,8,9]

# find index of number n in list
n = 3

left = 0
right = len(nums) - 1

index = binary_search_recursive(nums,n,left,right)

if index != -1:
    print("{} in numbers_list at index value {}".format(n,index))
else:
    print("{} is not in numbers_list".format(n))

    