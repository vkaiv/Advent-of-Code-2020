def partOne(lines):
    results = []
    for i in lines:
        qs = []
        for char in i:
            if not char in qs:
                qs.append(char)
        results.append(qs)
    results = sum([len(i) for i in results])
    return results

def partTwo(lines):
    count = 0
    for j in lines:
        lines = [{x for x in i} for i in j]
        a = lines[0].intersection(*lines)
        count += len(a)
    return count

with open('input.txt','r') as f:
    inputStr = f.read().split('\n\n')

lines1 = [i.replace('\n','') for i in inputStr]
lines2 = [i.replace('\n',' ').split(' ') for i in inputStr]

print(partTwo(lines2))
print(partOne(lines1))