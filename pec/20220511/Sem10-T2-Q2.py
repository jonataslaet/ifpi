age = int(input().strip())
bigger = age
lower = age
sum = 0
quantity = 0
if age == 0: 
    exit()

while(age != 0):
    quantity += 1
    sum += age
    if bigger > age:
        bigger = age
    if lower < age:
        lower = age
    age = int(input().strip())

print(quantity)
print(sum/quantity)
print(lower)
print(bigger)

