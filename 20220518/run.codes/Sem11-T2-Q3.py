#f(1) = 1
#f(2) = 1 + 1 / 2
#f(3) = f(2) + 1 / 3
#f(4) = f(3) + 1 / 4
#f(5) = f(4) + 1 / 5
#f(6) = f(5) + 1 / 6
#f(7) = f(6) + 1 / 7
#(...)
def f(n):
    if (n < 2):
        return 1
    elif (n == 2): 
        return 1 + (1/2)
    else:
        return f(n-1) + 1/n
    


if __name__ == "__main__":
    num = float(input().strip())
    print((f(num)))
