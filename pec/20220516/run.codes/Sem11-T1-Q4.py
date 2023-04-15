def luckNumberFromBirthday(data):
    #29041989
    t = len(data)
    sum = 0
    for i in range(0,t):
        sum += (int(data[i]))
    return sum


if __name__ == "__main__":
    birthday = (input().strip())
    print(luckNumberFromBirthday(birthday))
