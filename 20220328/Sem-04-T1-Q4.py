def segundosTotais(hh, mm, ss):
    return ss + (mm * 60) + (hh * 60 * 60)

if __name__ == "__main__":
    h = int(input())
    m = int(input())
    s = int(input())
    print(f'Passaram-se ', segundosTotais(h, m, s), ' desde a meia-noite')
