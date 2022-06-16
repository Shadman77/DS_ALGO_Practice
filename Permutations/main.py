def permutations_cus(nums):
    res = []
    if len(nums) == 1:
        return [nums[:]] # same as nums.copy but faster
    for i in range(len(nums)):
        temp = nums.pop(i)
        perms = permutations_cus(nums)
        for perm in perms:
            perm.insert(0, temp)
        res += perms
        nums.insert(i, temp)
    return res

if __name__ == "__main__":
    inp = [1,2,3]
    res = permutations_cus(inp)
    print(res)
