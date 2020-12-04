from passports import PassportChecker

def partOne(lines):
    reqFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    result = [li for li in lines if all(sub in li for sub in reqFields)]
    return result

def linesToDict(lines):
    lines = partOne(lines)
    lines = [i.split(' ') for i in lines]
    lines = [dict(i.split(':') for i in x) for x in lines]
    
    return lines

def partTwo(lines):
    linesDict = linesToDict(lines)
    count = 0
    for i in linesDict:
        passportCheck = PassportChecker(i)
        if all(passportCheck.testAll()):
            count += 1
    return count


with open('input.txt','r') as f:
    inputStr = f.read().split('\n\n')

lines = [i.replace('\n',' ') for i in inputStr]

print(f'Part one result: {len(partOne(lines))}')
print(f'Part two result: {partTwo(lines)}')