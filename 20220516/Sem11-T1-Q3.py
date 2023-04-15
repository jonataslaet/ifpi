def montante(b, i, t):
    return b*(i**t)

def trocaSeNecessario(a, b):
    if b > a:
        aux = b
        b = a
        a = aux
    return a,b


if __name__ == "__main__":
    # Ma = a*(1,02^t)
    # Mb = b*(1,03^t)
    #Mb >= Ma
    # b*(1,03^t) >= a*(1,02^t)
    a = int(input().strip())
    b = int(input().strip())
    a,b = trocaSeNecessario(a,b)
    t = 0
    while(montante(b, 1.03, t) < montante(a, 1.02, t)):
        t += 1

    print(t)
