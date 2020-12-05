def seatID(i):
    row = ''
    col = ''
    for char in i[:7]:
        if char == 'F': row += '0'
        if char == 'B': row += '1'
            
    for char in i[-3:]: 
        if char == 'L': col += '0'
        if char == 'R': col += '1'

    seatID = int(row,2) * 8 + int(col,2)
    return seatID

def mySeatID(ids):
    for i in range(6, len(ids)):
        if i != ids[i-6]:
            return i

with open('input.txt','r') as f:
    lines = f.readlines()

lines = [i.strip() for i in lines]
ids = sorted([seatID(i) for i in lines])
print(f'Highest seat number is: {ids[-1]}')
print(f'My seat number is: {mySeatID(ids)}')
