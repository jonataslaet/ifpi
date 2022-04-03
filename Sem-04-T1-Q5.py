def areaPiso(l, c):
    return l * c

def volumeSala(l, c, a):
    return l * c * a

def areaParedes(l, c, a):
    return 2 * a * l + 2 * a * c

if __name__ == "__main__":
   largura = float(input())
   altura = float(input())
   comprimento = float(input())
   print(f'Área do piso da sala: ', areaPiso(largura, altura))
   print(f'Volume da sala: ', volumeSala(largura, altura, comprimento))
   print(f'Área das paredes da sala: ', areaParedes(largura, altura, comprimento))
