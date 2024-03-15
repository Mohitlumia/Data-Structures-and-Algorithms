
def insertion_sort(elements):
    """
    insertion_sort has quadratic time and constant space complexity on average.
    
    Time Complexity:-
        Best Case:      O(n), when array is already sorted.
        Average Case:   O(n^2)
        Worst Case:     O(n^2)

    Space Complexity::- O(1)
    """
    n = len(elements)
    for i in range(1,n):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and elements[j] > anchor:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor


if __name__ == "__main__":
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)