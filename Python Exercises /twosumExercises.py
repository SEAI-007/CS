# Input: nums = [2,7,11,15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 9, so return [0, 1].

def twosums(nums, total=9):
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-1):
            j += 1
            if nums[i] + nums[j] == total:
                print(f"The positions are {i} and {j}.")
                break
            else: continue

twosums([2,6,11,1,62,25,7],9)