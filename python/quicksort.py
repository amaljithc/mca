def part(start,end,arr):
    pivotIndex=start
    pivot=arr[pivotIndex]
    while start<end:
        while start<len(arr) and arr[start]<=pivot:
            start += 1
        while arr[end]>pivot:
            end -= 1
        if start<end:
            arr[end],arr[start]=arr[start],arr[end]
    arr[end],arr[pivotIndex]=arr[pivotIndex],arr[end]
    return end
def sort(start,end,arr):
    if start<end:
        p=part(start,end,arr)
        sort(start,p-1,arr)
        sort(p+1,end,arr)
arr=[8,23,3,1,7]
sort(0,len(arr)-1,arr)
print(arr)

