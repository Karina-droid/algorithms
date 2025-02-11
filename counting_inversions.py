#count inversions in an array using merge sort
#O(n log n)

def countAndMerge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    left = arr[l:m+1]
    right = arr[m+1:r+1]

    result = 0
    i = 0
    j = 0
    k = l
    while (i < n1 and j < n2):
        #no increment in result if the left[] has a smaller or equal number than the right[]
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            result += (n1 - i)
        k += 1

    #merge remaining elements
    while(i < n1):
        arr[k] = left[i]
        i += 1
        k += 1
    while(j < n2):
        arr[k] = right[j]
        j += 1
        k += 1

    return result


def countInv(arr, l, r):
    result = 0
    if l < r:
        m = (l + r)//2

        #recursively count the inversions in the left and right halves
        result += countInv(arr, l, m)
        result += countInv(arr, m+1, r)
        result += countAndMerge(arr, l, m, r)
    return result

