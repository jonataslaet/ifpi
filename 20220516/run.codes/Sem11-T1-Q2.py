from math import ceil, log

if __name__ == "__main__":
    #Mp = 10000*(1,007^t)
    #Mc = c*(1,004^t)
    #Mp >= Mc
    #10000*(1,007^t) >= c*(1,004^t)
    #log(10000*(1,007^t)) >= log(c*(1,004^t))
    #t*(log(10000*(1,007))) >= t*(log(c*1,004))
    p = log(10070)
    c = float(input().strip())
    a = log(c*1.004)
    t = 0
    while(10000*(1.007**t) < c*(1.004**t)):
        t += 1
    
    print(t)

