def binary_search(arr, start, end, key): 
    if (start > end):
        return -1;

    mid = int(start + (end - start) / 2)

    if arr[mid] == key:
        return mid

    if arr[start] <= arr[mid] and key <= arr[mid] and key >= arr[start]:
        return binary_search(arr, start, mid - 1, key)

    elif arr[mid] <= arr[end] and key >= arr[mid] and key <= arr[end]: 
        return binary_search(arr, mid + 1, end, key)

    elif arr[end] <= arr[mid]:
        return binary_search(arr, mid + 1, end, key)

    elif arr[start] >= arr[mid]:
        return binary_search(arr, start, mid - 1, key)

    return -1;


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums,0,len(nums)-1,target)