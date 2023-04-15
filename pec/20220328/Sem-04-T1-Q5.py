def areaPiso(l, c):
    return l * c

def volumeSala(l, c, a):
    return l * c * a

def areaParedes(l, c, a):
    return 2 * a * l + 2 * a * c

if __name__ == "__main__":
   altura = float(input())
   comprimento = float(input())
   largura = float(input())
   print(f'Área do piso da sala: {areaPiso(largura, comprimento):0.0f}')
   print(f'Volume da sala: {volumeSala(largura, comprimento, altura):0.0f}')
   print(f'Área das paredes da sala: {areaParedes(largura, comprimento, altura):0.0f}')
