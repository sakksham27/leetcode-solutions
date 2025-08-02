# data structure: Hash map
# time complexity: O(n) -- Single pass through array 
# memory complexity: O(n) -- Storing entire array into hash map 

# Example values
nums = [2,7,11,15]
target = 9

eleHash = {} # Hash map which stores the index and value of each element in the array 

def twoSums(nums, target):
    for i,n in enumerate(nums):
        diff = target - n
        if diff in eleHash:
            return(eleHash[diff], i)
        eleHash[n] = i
    return

print(twoSums(nums, target))
 
