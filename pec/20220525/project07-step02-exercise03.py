def showIntroduction():
    print("Calculadora do Amor")
    print("<3 <3 <3 <3 <3 <3 <3")

def updateScoreByCriteria1(name, score):
    for char in name:
        if char in "aeiou":
            score += 5

def updateScoreByCriteria2(name, score):
    for char in name:
        if char in "amor":
            score += 10

def updateScore(name, score):
    score = updateScoreByCriteria1(name, score)
    score = updateScoreByCriteria2(name, score)
    if score < 10:
        print("Esqueça esta pessoa! Nunca vai dar certo!")
    return score

if __name__ == "__main__":
    showIntroduction()
    twoScores = [0, 0]
    twoPeople = input("Digite o nome de duas pessoas: ").strip().split(" e ")
    twoScores[0] = updateScore(twoPeople[0], twoScores[0])
    twoScores[1] = updateScore(twoPeople[1], twoScores[1])

