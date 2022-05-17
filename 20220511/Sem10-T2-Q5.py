def main():
    validScore = False
    while(validScore == False):
        score = float(input().strip())
        validScore = 0 <= score <= 10.0
        if (validScore):
            if (score >= 8.5):
                print('A')
            elif (score >= 7.0):
                print('B')
            elif (score >= 5.0):
                print('C')
            elif (score >= 4.0):
                print('D')
            elif (score >= 0.0):
                print('E')
        else:
            print('Nota inválida.')
        
if __name__ == "__main__":
    main()