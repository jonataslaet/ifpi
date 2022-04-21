def areaQuadrado(lado):
    return lado**2

def perimetroQuadrado(lado):
    return 4*lado

if __name__ == "__main__":
    l = float(input())
    aQ = areaQuadrado(l)
    pQ = perimetroQuadrado(l)
    print(f'{aQ:10.4f}')
    print(f'{pQ:10.4f}')
