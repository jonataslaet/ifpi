def getCelsius(t, e):
    if (e == 'C'):
        return t
    return round((t - 32) * (5/9), 4)


t1 = float(input().strip())
escalaT1 = input().upper()[0]

t2 = float(input().strip())
escalaT2 = input().upper()[0]

# Guarda em x e y o equivalente em celsius das temperaturas digitadas
x = getCelsius(t1, escalaT1)
y = getCelsius(t2, escalaT2)

# Começo considerando que a maior temperatura é a primeira digitada (junto com sua respectiva escala)
amaiortemperatura = round(t1, 4)
escaladamaiortemperatura = escalaT1

# Compara se o equivalente da segunda temperatura é maior,
# se for, atualizo a maior temperatura como sendo a segunda digitada e sua respectiva escala
if (y > x):
    amaiortemperatura = round(t2, 4)
    escaladamaiortemperatura = escalaT2

print(f'({amaiortemperatura}, \'{escaladamaiortemperatura}\')')
