nums = [2,7,11,15]
# nums = [2,7,4,9]
# nums = []

partner_list = []

def twoSum(nums, target):
    for num in nums:
        polo = target - num
        for num in nums:
            if num == polo:
                partner_list.append(nums.index(num))
    print(partner_list)


twoSum(nums =[3,3],target = 6)
# print(partner_list)
# new_list = twoSum(nums, target)
# Solution
# using a for loop means runtime is n^2 
# using a dictionary means n time

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            return([i,j]

seen = {}
for i,num in enumerate(nums):
    if target - num in seen:
        return([seen[target - num], i]) 
    elif num not in seen:
        seen[num] = i 


[1, 20],
[40, 46],
[34, 68],
[79, 86],
[148, 171],
[19, 190],
[14, 226],
[185, 233],
[37, 245],
[112, 274],
[236, 285],
[299, 324],
[322, 343],
[17, 354],
[88, 355],
[310, 369],
[135, 371],
[38, 380],
[41, 385],
[180, 397],
[109, 403],
[155, 405],
[384, 413],
[344, 445],
[187, 460],
[290, 464],
[283, 473],
[59, 502],
[280, 505],
[137, 518],
[176, 531],
[73, 562],
[475, 568]] 