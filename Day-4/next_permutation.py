def partition(arr, low, high):
	i = (low-1)		 
	pivot = arr[high]	 

	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)



def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if nums==sorted(nums,reverse=True):
            nums.reverse()
            print('1')
            return
        peakindex=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                peakindex=i
        #print(peakindex)
        if peakindex==0:
            nums.sort()
            
             
        prev_index=peakindex-1
        index=peakindex-1
        currindex=peakindex
        while currindex<len(nums) and nums[currindex]>nums[index]:
            previndex=currindex
            currindex+=1
            
        #print(currindex,previndex-1,index)
        nums[index],nums[previndex]=nums[previndex],nums[index]
        #print(nums,previndex)
        quickSort(nums,peakindex ,len(nums)-1)
        
        
        
        
