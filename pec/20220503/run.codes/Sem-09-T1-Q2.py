oddAmount = 0
evenAmount = 0
for n in range(1, 101):
    num = int(input())
    if (num % 2 == 0):
        evenAmount += 1
    else:
        oddAmount += 1
print(evenAmount)
print(oddAmount)
