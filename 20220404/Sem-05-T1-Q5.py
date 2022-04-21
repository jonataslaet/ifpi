def valorPagoAVista(v):
    return v * 0.91

def valorPagoEmCincoVezes(v):
    return v/5

def valorPagoEmDezVezes(v):
    return (v * 1.17)/10

val_compra = float(input().strip())
print(f'{valorPagoAVista(val_compra):0.2f}')
print(f'{valorPagoEmCincoVezes(val_compra):0.2f}')
print(f'{valorPagoEmDezVezes(val_compra):0.2f}')
