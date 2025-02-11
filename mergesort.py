#recurrence relation - T(n) = T(n/2) + O(n), complexity - O(n log n) 
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    #create temp arrays
    L = [0] * n1
    R = [0] * n2

    #copy the data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0   #initial index of the first subarray
    j = 0   #initial index of the second subarray
    k = left    #initial index of the merged subarray

    #merge the temp arrays back into arr[left..right]
    while(i < n1 and j < n2):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    #copy the remaining elements of L[], R[] if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1



def merge_sort(arr, left, right):
    if(left < right):
        mid = (left + right)//2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)