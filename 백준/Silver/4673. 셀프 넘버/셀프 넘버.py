nums = list(range(1,10000))
exc_nums = []

for num in nums:
    for n in str(num):
        num += int(n)
    exc_nums.append(num)

print(*sorted(set(nums)-set(exc_nums)), sep='\n')

