def formataHorario(horas):
    h = horas // 60
    m = horas  % 60
    return h,m

if __name__ == "__main__":
    horas = int(input())
    hh,mm = formataHorario(horas)
    print(f'{hh}:{mm}')
