from math import sqrt, ceil

def isPrime(num):
    raiz = sqrt(num+1)
    x = ceil(raiz)
    count = 0
    for i in range(1, x):
        if num % i == 0:
            count += 1
    return count == 1

if __name__ == "__main__":
    x = int(input().strip())
    y = int(input().strip())
    for n in range(x, y+1):
        if (isPrime(n)):
            print(n)