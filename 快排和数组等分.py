def quick_sort(lst):
    if not lst:
        return []
    pivot = lst[0]
    left = quick_sort([x for x in lst[1: ] if x < pivot])
    right = quick_sort([x for x in lst[1: ] if x >= pivot])
    return left + [pivot] + right

# 随后总结
def canPartition(nums):
    if nums = []:
        return True
    if sum(nums)%2 == 1:
        return False
    target = sum(nums)/2
    dp = [0 for i in range(target+1)]
    dp[0] = 1
    for n in nums:
        tar_temp = target
        while tar_temp >= n:
            dp[tar_temp] = dp[tar_temp] + dp[tar_temp - n]
            tar_temp = tar_temp - 1
    if dp[target] == 0:
        return False
    else:
        return True
            
