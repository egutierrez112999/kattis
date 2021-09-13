nums = input().split()
num1 = nums[0]
num2 = nums[1]
new1 = num1[2]+num1[1]+num1[0]
new2 = num2[2]+num2[1]+num2[0]
if int(new1) > int(new2):
    print(new1)
else:
    print(new2)
