nums = input().split()
x = int(nums[0])
y = int(nums[1])
n = int(nums[2])
for i in range(n):
    i+= 1
    if i%y == 0 and i%x == 0:
        print('FizzBuzz')
    elif i%y == 0:
        print('Buzz')
    elif i%x == 0:
        print('Fizz')
    else:
        print(i)
