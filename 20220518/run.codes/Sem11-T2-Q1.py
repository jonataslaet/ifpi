def fat(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fat(n-1)


if __name__ == "__main__":
    num = int(input().strip())
    print(fat(num))
