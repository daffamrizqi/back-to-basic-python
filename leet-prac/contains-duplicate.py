def containsDuplicate(nums: list):
    hashset = set()
    for item in nums:
        if item in hashset:
            return True
        hashset.add(item)
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3]))