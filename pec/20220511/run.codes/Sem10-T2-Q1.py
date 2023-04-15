
num = int(input().strip())
flag = num != 0

sum = 0
while(flag):
    sum += num
    num = int(input().strip())
    flag = num != 0

print(sum)
