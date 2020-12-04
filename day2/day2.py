def passwordCheck(password):
    lowerLimit = ''
    upperLimit = ''
    reachedDash = False
    reachedColon = False
    char = ''
    count = 0
    partOneValid = False
    partTwoValid = False
    colonIndex = password.find(':')
    for i in password:
        if i == ':': reachedColon = True
        if i == '-': reachedDash = True
        if i.isnumeric():
            if not reachedDash:
                lowerLimit += i
            else:
                upperLimit += i
        if i.isalpha() and not reachedColon:
            char = i
        
        if i.isalpha() and reachedColon:
            if i == char:
                count += 1
    
    if count >= int(lowerLimit) and count <= int(upperLimit):
        partOneValid = True

    if (password[int(lowerLimit)+colonIndex+1] == char) ^ (password[int(upperLimit)+colonIndex+1] == char):
        partTwoValid = True
    
    return partOneValid, partTwoValid

def main():
    with open('input.txt', 'r') as fh:
        passwords = fh.readlines()

    passwords = [i.strip() for i in passwords]
    passedPartOne = 0
    passedPartTwo = 0
    for i in passwords:
        result = passwordCheck(i)
        if result[0]:
            passedPartOne += 1
        if result[1]:
            passedPartTwo += 1

    print(f'The number of valid passwords for part one is {passedPartOne}')
    print(f'The number of valid passwords for part two is {passedPartTwo}')

if __name__ == '__main__':
    main()