def reverseNumber(x):
    num = x
    numberText = ''
    if (num < 0):
        numberText += '-'
        num *= (-1)
    while(num > 9):
        numberText += str(num % 10)
        num //= 10
    numberText += str(num % 10)
    return int(numberText)

if __name__ == "__main__":
    number = int(input().strip())
    print(reverseNumber(number))