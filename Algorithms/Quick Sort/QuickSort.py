
def swap(a,b,elements):
    temp = elements[a]
    elements[a] = elements[b]
    elements[b] = temp


def partion(start,end,elements):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1
        if start < end:
            swap(start,end,elements)

    swap(pivot_index,end,elements)
    
    return end

def quick_sort(start,end,elements):
    
    if start < end:
        pi = partion(start,end,elements)
        quick_sort(start,pi-1,elements)
        quick_sort(pi+1,end,elements)

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    size = len(elements)-1
    quick_sort(0,size,elements)
    print(elements)