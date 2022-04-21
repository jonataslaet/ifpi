def isPar(num):
    return num % 2 == 0


def temDoisDigitos(num):
    return num > 9 and num < 100


if __name__ == "__main__":
    num = int(input().strip())
    #78
    d1 = (num//10) #78/10= 8
    d2 = num % 10 #78 % 10 = 8
        
    if (temDoisDigitos(num) and isPar(d1) and isPar(d2)): 
        print("Nenhum dígito é ímpar.")
    elif (temDoisDigitos(num) and ((not isPar(d1) and isPar(d2))or(not isPar(d2) and isPar(d1)))): 
        print("Apenas um dígito é ímpar.")
    elif (temDoisDigitos(num) and (not isPar(d1) and not isPar(d2))): 
        print("Os dois dígitos são ímpares.")
