

num = 5
array = [1,2,3,4,5,6,7,8,9,10]

# binarySearch num in sorted array "array and print its index value

left = 0
right = len(array)-1

while not left == right:

    midPtr = (right-left)//2

    if array[midPtr] == num:
        break
    elif array[midPtr] > num:
        right = midPtr
    else:
        left = midPtr + 1

if array[midPtr] == num:
    print("{} in array at index value {}".format(num,midPtr))
else:
    print("{} is not in array".format(num))
