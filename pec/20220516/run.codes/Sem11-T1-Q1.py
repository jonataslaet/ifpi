from math import ceil


if __name__ == "__main__":
    #sTartaruga = s0Tartaruga + vTartatura * t
    #sLebre = s0Lebre + vLebre * t
    #sLebre >= sTartaruga
    #s0Lebre + vLebre * t >= s0Tartaruga + vTartatura * t
    #s0Lebra = 0
    #vLebre = 10
    #vTartaruga = 1
    #10 * t >= s0Tartaruga + 1 * t
    #10 * t - t >= s0Tartaruga
    #t*(10 - 1) >= s0Tartaruga
    #9*t >= s0Tartaruga
    #t >= s0Tartaruga/9
    s0Tartatura = float(input().strip())
    print(ceil(s0Tartatura/9))
