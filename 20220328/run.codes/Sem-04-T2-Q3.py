def precoComDesconto(p, v):
    return p * (1 - (v/100))

def precoAcrescido(p, v):
    return p * (1 + (v/100))

if __name__ == "__main__":
    preco = float(input())
    valorPercentual = float(input())
    y = precoAcrescido(preco,valorPercentual)
    x = precoComDesconto(preco,valorPercentual)
    print(f'{y:0.2f}')
    print(f'{x:0.2f}')
    
