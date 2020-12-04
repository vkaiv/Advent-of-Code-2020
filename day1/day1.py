def findSum(lines):
    for i in lines:
        for j in lines:
            if i + j == 2020:
                print(f"{i} + {j} = {i+j}")
                print(f"{i} * {j} = {i*j}")
                
            for k in lines:
                if i + j + k == 2020:
                    print(f"{i} + {j} + {k} = {i+j+k}")
                    print(f"{i} * {j} + {k} = {i*j*k}")
                    return

filename = 'input.txt'
with open(filename, 'r') as fh:
    lines = fh.readlines()

lines = [int(i.strip()) for i in lines]
findSum(lines)