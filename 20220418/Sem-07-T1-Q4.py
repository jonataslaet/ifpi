def averageOf5(n1, n2, n3, n4, n5):
    soma = n1 + n2 + n3 + n4 + n5
    media = soma / 5
    return media

if __name__ == "__main__":
    num1 = float(input().strip())
    num2 = float(input().strip())
    num3 = float(input().strip())
    num4 = float(input().strip())
    num5 = float(input().strip())
    media = averageOf5(num1, num2, num3, num4, num5)
    print(f'{media:0.2f}')
    if (num1 > media): print(f'{num1:0.2f}')
    if (num2 > media): print(f'{num2:0.2f}')
    if (num3 > media): print(f'{num3:0.2f}')
    if (num4 > media): print(f'{num4:0.2f}')
    if (num5 > media): print(f'{num5:0.2f}')