from math import log, ceil

c = float(input().strip())
i = float(input().strip())
i = i / 100.0
# 2*C = C*(1+i)^t
# 2 = (1+i)^t
# (1+i)^t = 2
# log(1+i)^t = log2
# t*log(1+i) = log2
# t = (log(2)) / (log(1+i))
anosOuAno = 'anos'
t = ceil((log(2)) / (log(1+i)))
if t == 1:
    anosOuAno = 'ano'
print(f'R${c:.2f} rendendo {i*100:.0f}% ao ano irá dobrar em {t} {anosOuAno}.')
