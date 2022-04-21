def segundosTotais(hh, mm, ss):
    return ss + (mm * 60) + (hh * 60 * 60)

if __name__ == "__main__":
    h = int(input())
    m = int(input())
    s = int(input())
    print(segundosTotais(h, m, s))
