from math import sqrt, ceil
def isPrime(num):
    
    raiz = sqrt(num)
    x = ceil(raiz)
    
    count = 0
    for i in range(1, x+1):
        if num % i == 0:
            count += 1
    return count == 1

if __name__ == "__main__":
    num = float(input().strip())
    print(isPrime(num))