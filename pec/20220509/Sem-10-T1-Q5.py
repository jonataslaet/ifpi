def getNextMonthAndYear(m, y):
    if m+1 > 12:
        return 1,y+1
    return m+1,y

if __name__ == "__main__":
    initialSalary = float(input().strip())
    initialDebit = float(input().strip())
    month = 10
    year = 2016
    i = 1
    currentSalary = initialSalary * (1.05**(year-2016))
    currentDebit = initialDebit * (1.15**i)
    while(currentDebit <= currentSalary):
        month, year = getNextMonthAndYear(month, year)
        currentSalary = initialSalary * (1.05**(year-2016))
        currentDebit = initialDebit * (1.15**i)
        i+=1
    print(month)
    print(year)


