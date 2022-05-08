def traffic(x):
    c = x.upper()
    if (c == "V"): print("Siga")
    elif (c == "A"): print("Atenção")
    else: print("Pare")

if __name__ == "__main__":
    cor = input().strip()
    traffic(cor)
