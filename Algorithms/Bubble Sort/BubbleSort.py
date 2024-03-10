

def BubbleSort(elements):
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