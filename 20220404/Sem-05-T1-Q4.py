def soma(num1, num2, num3, num4, num5):
    return num1 + num2 + num3 + num4 + num5

def avgOf5(a, b, c, d, e):
    return soma(a,b,c,d,e) / 5

n1 = int(input().strip())
n2 = int(input().strip())
n3 = int(input().strip())
n4 = int(input().strip())
n5 = int(input().strip())
print(max(n1, n2, n3, n4, n5))
print(min(n1, n2, n3, n4, n5))
print(avgOf5(n1, n2, n3, n4, n5))
