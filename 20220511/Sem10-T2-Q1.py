
num = int(input().strip())
flag = num != 0
if (flag == False):
    exit()
sum = 0
while(flag):
    sum += num
    num = int(input().strip())
    flag = num != 0

print(sum)
