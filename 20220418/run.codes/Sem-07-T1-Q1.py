diaAtual = int(input().strip())
mesAtual = int(input().strip())
anoAtual = int(input().strip())
diaNasc = int(input().strip())
mesNasc = int(input().strip())
anoNasc = int(input().strip())

result = anoAtual - anoNasc
if ((mesAtual < mesNasc) or (diaAtual < diaNasc)): result = result - 1
print(result)