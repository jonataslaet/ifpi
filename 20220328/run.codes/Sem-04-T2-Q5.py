def numeroAoContrario(number):
    a4 = number//1000
    a3 = (number//100) % 10
    a2 = (number//10) % 10
    a1 = number % 10
    return a1*1000 + a2*100 + a3*10 + a4

if __name__ == "__main__":
    number = int(input())
    print(numeroAoContrario(number))
