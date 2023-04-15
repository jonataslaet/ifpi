if __name__ == "__main__":
    p = int(input().strip())
    a = 1600
    original = p
    # não menor = maior ou igual
    # se p < 10% de original, pare = quando cair para menos de 10% da original, pare
    while (p >= 0.1 * original):
        n = 0.01 * p
        m = 0.06 * p
        p = p + n - m
        print(f'{a},{n:.0f},{m:.0f},{p:.0f}')
        a += 1
