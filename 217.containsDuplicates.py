# data structure: Hash map 
# time complexity: O(n)
# space complextiy: O(n)

# Example
nums = [2,14,18,22,22]

def containsDuplicates(nums):
    tempHash = {}
    tempHash[nums[0]] = 0
    for i, n in enumerate(nums[1:]):
        if(n in tempHash):
            return True
            break
        else: 
            tempHash[n] = i
    return False
    
print(containsDuplicates(nums))
    
