

def BubbleSort(elements):
    """
    BubbleSort has quadratic time and constant space complexity on average.
    
    Time Complexity:-
        Best Case:      O(n), when array is already sorted.
        Average Case:   O(n^2)
        Worst Case:     O(n^2)

    Space Complexity::- O(1)
    """
    size = len(elements)
    for _ in range(size-1):
        swaped = False
        # swap two consicutive elements if not sorted
        for i in range(size-1):
            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swaped = True
        # if no elements swaped means all elements are sorted
        if not swaped:
            break

if __name__ == '__main__':

    elements = [5,2,4,1,0,2,6,7,9,8]

    BubbleSort(elements)
    print(elements)