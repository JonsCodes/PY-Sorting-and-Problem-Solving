# Write your solution for algorithm 5 below

def find_pair_with_sum(nums, target):
    nums.sort()
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return nums[left], nums[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return "no pairs sum to the target"

sample_nums = [5, 10, 4, 7, 6, 2]
sample_target = 9
print(find_pair_with_sum(sample_nums, sample_target))  # Expected output: (2, 7)
