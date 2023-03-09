for i in range(0, nums - 1):
    for j in range(i + 1, nums):
        if nums[i] + nums[j] == target:
            return result[i][j];
