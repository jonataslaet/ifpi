num1 = int(input().strip())
num2 = int(input().strip())
num3 = int(input().strip())
num4 = int(input().strip())
num5 = int(input().strip())
biggestNumber = num1
shortestNumber = num1
if (num2 > biggestNumber): 
    biggestNumber = num2
if (num3 > biggestNumber): 
    biggestNumber = num3
if (num4 > biggestNumber): 
    biggestNumber = num4
if (num5 > biggestNumber): 
    biggestNumber = num5

if (num2 < shortestNumber): 
    shortestNumber = num2
if (num3 < shortestNumber): 
    shortestNumber = num3
if (num4 < shortestNumber): 
    shortestNumber = num4
if (num5 < shortestNumber): 
    shortestNumber = num5
print(biggestNumber)
print(shortestNumber)