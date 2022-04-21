dia = int(input().strip())
mes = int(input().strip())

if (dia>=21 and mes==3) or (dia<=19 and mes==4):
    print ('Áries')
if (dia>=20 and mes==4) or (dia<=20 and mes==5):
    print ('Touro')
if (dia>=21 and mes==5) or (dia<=21 and mes==6):
    print ('Gêmeos')
if (dia>=22 and mes==6) or (dia<=22 and mes==7):
    print ('Câncer')
if (dia>=23 and mes==7) or (dia<=22 and mes==8):
    print ('Leão')
if (dia>=23 and mes==8) or (dia<=22 and mes==9):
    print ('Virgem')
if (dia>=23 and mes==9) or (dia<=22 and mes==10):
    print ('Libra')
if (dia>=23 and mes==10) or (dia<=21 and mes==11):
    print ('Escorpião')
if (dia>=22 and mes==11) or (dia<=21 and mes==12):
    print ('Sagitário')
if (dia>=22 and mes==12) or (dia<=19 and mes==1):
    print ('Capricórnio')
if (dia>=20 and mes==1) or (dia<=18 and mes==2):
    print ('Aquário')
if (dia>=19 and mes==2) or (dia<=20 and mes==3):
    print ('Peixes')