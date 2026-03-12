def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        minimum=i

        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum=j
        if minimum != i:
            arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr
arr=[64,25,12,34,23,90]
print(selection_sort(arr))