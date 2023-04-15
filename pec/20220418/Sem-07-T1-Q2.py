diaX = int(input().strip())
mesX = int(input().strip())
anoX = int(input().strip())
diaY = int(input().strip())
mesY = int(input().strip())
anoY = int(input().strip())

recentDate = f'{diaX}/{mesX}/{anoX}'
if (anoY > anoX): 
    recentDate = f'{diaY}/{mesY}/{anoY}'
elif (anoY == anoX): 
    if (mesY > mesX): 
        recentDate = f'{diaY}/{mesY}/{anoY}'
    elif (mesY == mesX): 
        if (diaY > diaX): 
            recentDate = f'{diaY}/{mesY}/{anoY}'
print(recentDate)