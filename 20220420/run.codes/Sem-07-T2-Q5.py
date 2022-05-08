if __name__ == "__main__":
    num1 = int(input().strip())
    num2 = int(input().strip())
    num3 = int(input().strip())
    if (num1 < num2 < num3):
        print(num1)
        print(num2)
        print(num3)
    elif (num1 < num3 < num2):
        print(num1)
        print(num3)
        print(num2)
    elif (num2 < num1 < num3):
        print(num2)
        print(num1)
        print(num3)
    elif (num2 < num3 < num1):
        print(num2)
        print(num3)
        print(num1)
    elif (num3 < num2 < num1):
        print(num3)
        print(num2)
        print(num1)
    else: 
        print(num3)
        print(num1)
        print(num2)